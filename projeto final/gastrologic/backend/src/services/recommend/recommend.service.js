// src/services/recommend/recommend.service.js
import { getNutrition } from "../nutrition/nutrition.service.js";
import {
  calculateRecipeTotals,
  calculateMacroPercentages
} from "./macros.service.js";
import { resolveIngredient } from "./ingredient.service.js";
import {
  searchMealsByIngredient,
  getMealDetailsById,
  extractMealIngredients,
  ingredientMatches
} from "./themealdb.service.js";

// Normaliza texto para comparação
function normalizeText(text) {
  return (text || "").toLowerCase().trim();
}

function getSubstitute(ingredient) {
  const map = {
    chicken: "tofu",
    beef: "lentils",
    milk: "almond milk",
    butter: "olive oil",
    rice: "quinoa"
  };

  const key = ingredient.toLowerCase();

  return map[key] || null;
}

function getMockNutritionForIngredient(ingredient) {
  const nutritionTable = {
    chicken: { calories: 165, protein: 31, carbs: 0, fat: 3.6 },
    tomato: { calories: 18, protein: 0.9, carbs: 3.9, fat: 0.2 },
    garlic: { calories: 149, protein: 6.4, carbs: 33.1, fat: 0.5 },
    onion: { calories: 40, protein: 1.1, carbs: 9.3, fat: 0.1 },
    rice: { calories: 130, protein: 2.7, carbs: 28, fat: 0.3 },
    potato: { calories: 77, protein: 2, carbs: 17, fat: 0.1 },
    beef: { calories: 250, protein: 26, carbs: 0, fat: 15 },
    cheese: { calories: 402, protein: 25, carbs: 1.3, fat: 33 },
    egg: { calories: 155, protein: 13, carbs: 1.1, fat: 11 },
    milk: { calories: 42, protein: 3.4, carbs: 5, fat: 1 }
  };

  const normalized = normalizeText(ingredient);

  return (
    nutritionTable[normalized] || {
      calories: 0,
      protein: 0,
      carbs: 0,
      fat: 0
    }
  );
}

function calculateMacroScore(macro, profile) {
  const targets = {
    balanced: { protein: 15, carbs: 55, fat: 30 },
    high_protein: { protein: 30, carbs: 40, fat: 30 },
    low_carb: { protein: 30, carbs: 20, fat: 50 }
  };

  const target = targets[profile];
  if (!target) return 0;

  const diff =
    Math.abs(macro.protein - target.protein) +
    Math.abs(macro.carbs - target.carbs) +
    Math.abs(macro.fat - target.fat);

  return Math.max(0, 100 - diff);
}

function removeDuplicateMeals(meals) {
  return [...new Map(meals.map(meal => [meal.idMeal, meal])).values()];
}

function countMatchedIngredients(mealIngredients, resolvedIngredients) {
  let matchCount = 0;

  for (const ingredient of resolvedIngredients) {
    const found = ingredientMatches(mealIngredients, ingredient.english);
    if (found) {
      matchCount++;
    }
  }

  return matchCount;
}

function passesBasicFilters(totals, filters = {}) {
  if (filters.maxCalories && totals.calories > filters.maxCalories) {
    return false;
  }

  if (filters.minProtein && totals.protein < filters.minProtein) {
    return false;
  }

  if (filters.maxCarbs && totals.carbs > filters.maxCarbs) {
    return false;
  }

  if (filters.maxFat && totals.fat > filters.maxFat) {
    return false;
  }

  return true;
}

function getDietScore(mealIngredients, profile) {
  const ingredientsLower = mealIngredients.map(i =>
    normalizeText(i).replace(/[^a-z\s]/g, "")
  );
  const nonVegetarian = [
    "chicken", "beef", "pork", "fish",
    "ham", "bacon", "sausage", "tuna", "salmon"
  ];
  const nonVegan = [
    ...nonVegetarian,
    "milk", "egg", "cheese", "butter", "cream", "honey"
  ];

  let penalty = 0;

  for (const ing of ingredientsLower) {
    if (profile === "vegetarian") {
      if (nonVegetarian.some(item => ing.includes(item))){
        return 0; // penaliza fortemente receitas com carne para vegetarianos 
      };
    }

    if (profile === "vegan") {
      if (nonVegan.some(item => ing.includes(item))){
        return 0; // penaliza fortemente receitas com ingredientes de origem animal para veganos
      };
    }
  }

  return Math.max(0, 10 - penalty);
}

export async function recommendRecipes({
  ingredients = [],
  profile = "balanced",
  filters = {}
}) {
  const resolvedIngredients = [];

  // 1. Resolver/traduzir ingredientes recebidos do frontend
  for (const input of ingredients) {
    const resolved = await resolveIngredient(input);
    if (resolved?.english) {
      resolvedIngredients.push(resolved);
    }
  }

  const validMeals = [];

  // 2. Procurar receitas na TheMealDB
  const mealResults = await Promise.all(
    resolvedIngredients.map(async i => {
      const meals = await searchMealsByIngredient(i.english);
      return meals.slice(0, 10); // máximo 10 receitas por ingrediente
    })
  );

  const allMeals = mealResults.flat().slice(0, 30); // Limitar a 30 receitas por ingrediente para performance

  const uniqueMealsFromAPI = [
    ...new Map(allMeals.map(meal => [meal.idMeal, meal])).values()
  ];

  const detailedMeals = await Promise.all(
    uniqueMealsFromAPI.map(meal => getMealDetailsById(meal.idMeal))
  );

  const validDetails = detailedMeals.filter(Boolean);

  for (const details of validDetails) {
    const mealIngredients = extractMealIngredients(details);    
    
    const hasMainIngredient = resolvedIngredients.some(ing =>
      ingredientMatches(mealIngredients, ing.english)
    );

    if (!hasMainIngredient) continue;

    const matchCount = countMatchedIngredients(
      mealIngredients,
      resolvedIngredients
    );

    const dietScore = getDietScore(mealIngredients, profile);
    
    if (profile === "vegan" && dietScore < 5) continue;
    if (profile === "vegetarian" && dietScore < 5) continue;

    // evita receitas com poucos ingredientes relevantes
    if (matchCount < 1) continue;

    // para performance → só alguns ingredientes na nutrição
    const limitedIngredients = mealIngredients.slice(0, 6);

    // 4. Obter nutrição dos ingredientes da receita
    const nutritionData = await Promise.all(
      limitedIngredients.map(async item => {
        try {
          return await getNutrition(item);
        } catch {
          return getMockNutritionForIngredient(item);
        }
      })
    );

    // 5. Calcular totais e percentagens
    const nutrition = calculateRecipeTotals(nutritionData);
    const macroPercentages = calculateMacroPercentages(nutrition);

    // 6. Aplicar score de macros apenas para perfis específicos
    let macroScore = 0;
    if (["balanced", "high_protein", "low_carb"].includes(profile)) {
      macroScore = calculateMacroScore(macroPercentages, profile);
    }

    // 7. Aplicar filtros adicionais
    if (!passesBasicFilters(nutrition, filters)) {
      continue;
    }    

    validMeals.push({
      idMeal: details.idMeal,
      name: details.strMeal,
      category: details.strCategory,
      area: details.strArea,
      instructions: details.strInstructions,
      thumbnail: details.strMealThumb,
      youtube: details.strYoutube,
      ingredients: mealIngredients,
      matchedIngredient: resolvedIngredients.map(i => i.english),
      matchCount,
      nutrition,
      macroPercentages,
      macroScore,
      dietScore,
      substitutes: mealIngredients.map(ing => ({
        original: ing,
        substitute: getSubstitute(ing)
      }))
    });
  }

  const uniqueMeals = removeDuplicateMeals(validMeals);
  
  if (uniqueMeals.length === 0 && profile !== "balanced") {
    console.log("⚠️ fallback sem filtro de dieta");

    return recommendRecipes({
      ingredients,
      profile: "balanced",
      filters
    });
  }

  uniqueMeals.sort(
    (a, b) =>
      b.matchCount - a.matchCount ||
      b.macroScore - a.macroScore ||
      b.dietScore - a.dietScore
  );

  return {
    message: "Recomendação gerada com sucesso",
    profile,
    filtersApplied: filters,
    resolvedIngredients,
    totalRecipes: uniqueMeals.length,
    meals: uniqueMeals.slice(0, 9) // Limitar a 9 receitas finais 
  };
}
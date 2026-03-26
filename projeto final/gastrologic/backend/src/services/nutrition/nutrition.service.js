import { getUSDAData } from "./usda.service.js";
import { getOFFData } from "./openfoodfacts.service.js";
import { normalizeIngredientName } from "../recommend/ingredientNormalizer.js";

const DEBUG = false;
const cache = new Map();

function estimateGrams(ingredient) {
  const name = (ingredient || "").toLowerCase();

  if (name.includes("oil")) return 10;
  if (name.includes("chicken")) return 150;
  if (name.includes("rice")) return 100;
  if (name.includes("onion")) return 80;
  if (name.includes("garlic")) return 5;
  if (name.includes("butter")) return 15;
  if (name.includes("milk")) return 100;

  return 50; // default
}

function normalize(data, ingredient) {
  const grams = estimateGrams(ingredient);
  const factor = grams / 100;

  return {
    calories: (data?.calories || 0) * factor,
    protein: (data?.protein || 0) * factor,
    carbs: (data?.carbs || 0) * factor,
    fat: (data?.fat || 0) * factor
  };
}

function getMockNutrition() {
    return {
    calories: 100,
    protein: 10,
    carbs: 10,
    fat: 5
    };
}

export async function getNutrition(ingredient) {
    const cleanIngredient = normalizeIngredientName(ingredient);
    const key = (cleanIngredient || "").toLowerCase();

    if (cache.has(key)) {
        if (DEBUG) console.log(`🟡 CACHE usado para ${cleanIngredient}`);
        return cache.get(key);
    }

    // 🥇 USDA
    try {
        const usda = await getUSDAData(cleanIngredient);

        if (usda) {
            if (DEBUG) console.log(`🟢 USDA usado para ${cleanIngredient}`);

            const normalized = normalize(usda, ingredient);
            cache.set(key, normalized);

            return normalized;
        }
    } catch (e) {
        if (DEBUG) console.log(`🔴 USDA erro (${cleanIngredient})`);
    }

    // 🥈 Open Food Facts
    try {
        const off = await getOFFData(cleanIngredient);

        if (off) {
            if (DEBUG) console.log(`🟠 OFF usado para ${cleanIngredient}`);

            const normalized = normalize(off, ingredient);
            cache.set(key, normalized);

            return normalized;
        }
    } catch (e) {
        if (DEBUG) console.log(`🔴 OFF erro (${cleanIngredient})`);
    }

    // 🥉 Mock
    if (DEBUG) console.log(`⚪ Mock usado para ${cleanIngredient}`);

    const normalized = normalize(getMockNutrition(), ingredient);
    cache.set(key, normalized);

    return normalized;
}

console.log("nutrition service carregado");
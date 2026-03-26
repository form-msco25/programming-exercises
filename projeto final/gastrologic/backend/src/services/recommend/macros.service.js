// backend/src/services/recommend/macros.service.js

function calculateRecipeTotals(nutritionData = []) {
  let calories = 0;
  let protein = 0;
  let carbs = 0;
  let fat = 0;

  for (const item of nutritionData) {
    calories += Number(item.calories || 0);
    protein += Number(item.protein || 0);
    carbs += Number(item.carbs || 0);
    fat += Number(item.fat || 0);
  }

  return {
    calories: round(calories),
    protein: round(protein),
    carbs: round(carbs),
    fat: round(fat)
  };
}

function calculateMacroPercentages(totals = {}) {
  const proteinKcal = Number(totals.protein || 0) * 4;
  const carbsKcal = Number(totals.carbs || 0) * 4;
  const fatKcal = Number(totals.fat || 0) * 9;

  const totalMacroKcal = proteinKcal + carbsKcal + fatKcal;

  if (totalMacroKcal === 0) {
    return {
      protein: 0,
      carbs: 0,
      fat: 0
    };
  }

  return {
    protein: round((proteinKcal / totalMacroKcal) * 100),
    carbs: round((carbsKcal / totalMacroKcal) * 100),
    fat: round((fatKcal / totalMacroKcal) * 100)
  };
}

function round(value) {
  return Number(value.toFixed(1));
}

export {
  calculateRecipeTotals,
  calculateMacroPercentages
};
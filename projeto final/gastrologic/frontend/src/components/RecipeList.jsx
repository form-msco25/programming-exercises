import RecipeCard from "./RecipeCard";

const RecipeList = ({ lista }) => {

  if (!lista || lista.length === 0) {
    return null;
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 max-w-7xl w-full mx-auto place-items-center px-6 mt-10">
      {lista.map((rec) => (
        <RecipeCard key={rec.idMeal} rec={rec} />
      ))}
    </div>
  );
};

export default RecipeList;
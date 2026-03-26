import { useNavigate } from "react-router-dom";

const getScoreColor = (score) => {
  if (score > 80) return "bg-green-100 text-green-700";
  if (score > 60) return "bg-yellow-100 text-yellow-700";
  return "bg-red-100 text-red-700";
};

const RecipeCard = ({ rec }) => {
    const navigate = useNavigate();
    return (
    <section className="relative bg-white/60 backdrop-blur-md rounded-3xl shadow-xl p-6 w-full max-w-xs flex flex-col items-center">
        {rec?.macroScore > 80 && (
            <span className="absolute top-2 right-2 bg-yellow-400 text-white text-xs px-2 py-1 rounded-full shadow">
                ⭐ Top Match
            </span>
        )}
        {/* Imagem */}
        <div className="w-32 h-32 mb-4">
            <img
                src={rec?.thumbnail}
                alt={rec?.name}
                className="w-full h-full object-contain drop-shadow-xl"
            />
        </div>

        {/* Conteúdo */}
        <div className="text-center flex flex-col flex-grow">

            {/* Nome */}
            <h3 className="font-bold text-xl leading-tight mb-2">
                {rec?.name}
            </h3>

            {/* Categoria */}
            <span className="text-xs opacity-70 mb-3">
                {rec?.area} • {rec?.category}
            </span>

            {/* Nutrição */}
            <div className="flex flex-wrap justify-center gap-2 mb-4">                
                {rec?.macroScore > 0 && (
                    <div className="mb-3">
                        <span className={`${getScoreColor(rec.macroScore)} px-3 py-1 rounded-full text-sm font-semibold shadow-sm`}>
                            ⭐ {Math.round(rec.macroScore)}% Match Nutricional
                        </span>
                    </div>
                )}
            
                <span className="badge bg-orange-100 text-orange-600">
                🔥 {rec?.nutrition?.calories ?? 0} kcal
                </span>
                <span className="badge bg-green-100 text-green-600">
                💪 {rec?.nutrition?.protein ?? 0}g
                </span>
                <span className="badge bg-blue-100 text-blue-600">
                🥑 {rec?.nutrition?.fat ?? 0}g
                </span>
                <span className="badge bg-yellow-100 text-yellow-600">
                🍞 {rec?.nutrition?.carbs ?? 0}g
                </span>
            </div>

            {/* Label perfil */}
            {rec?.macroPercentages?.protein > 30 && (
                <span className="text-xs bg-blue-100 px-2 py-1 rounded-full mb-3 self-center">
                High Protein
                </span>
            )}

            {/* Botão */}
            <div className="mt-auto w-full flex justify-between items-center border-t pt-4">
                <span className="font-bold text-lg">Ver Mais</span>
                <button onClick={() => navigate(`/recipe/${rec.idMeal}`, { state: { recipe: rec } })}
                    className="w-10 h-10 rounded-xl flex items-center justify-center font-bold text-xl bg-berry-500 text-white hover:bg-berry-600 shadow-md transition-colors">
                +
                </button>
            </div>
        </div>
    </section>
  );
};
export default RecipeCard;
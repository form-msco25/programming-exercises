// Serviço API
import { useState } from "react";
import { recommendRecipes } from "../services/api";
// componentes
import Nav from '../components/Nav';
import Hero from '../components/Hero';
import IngredientsInput from '../components/IngredientsInput';
import RecipeList from '../components/RecipeList';
import RecipeGenerator from '../components/RecipeGenerator';
import Footer from '../components/Footer';
// dados de testar front

function HomePage() {

  const [ingredientes, setIngredientes] = useState([]);
  const [recipes, setRecipes] = useState([]);
  const [perfil, setPerfil] = useState("balanced");

  async function handleGenerateRecipes(ingredientes) {//função para chamar backend e obter receitas recomendadas com base nos ingredientes do usuário
    try {
      const data = await recommendRecipes(ingredientes, perfil); //chama função do serviço API para obter receitas recomendadas
      const sortedMeals = (data.meals || []).sort(
        (a, b) => b.macroScore - a.macroScore
      );
      setRecipes(sortedMeals);  //atualiza estado com as receitas recomendadas
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div>
      <Nav />
      <Hero />
      <main 
        className="relative min-h-screen w-full bg-cover bg-center bg-no-repeat flex flex-col items-start justify-start overflow-hidden" 
        style={{ backgroundImage: "url('/images/fundo_hero_2.webp')" }}
      >
        <IngredientsInput setIngredientes={setIngredientes} setPerfil = {setPerfil} />

        <RecipeGenerator
          ingredientes={ingredientes}
          profile={perfil}
          onGenerate={handleGenerateRecipes}
        />

        <RecipeList lista={recipes} />
      </main>
    </div>
  );
}

export default HomePage;
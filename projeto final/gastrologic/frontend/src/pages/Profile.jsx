import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const ProfilePage = () => {
  const navigate = useNavigate();
  const user = JSON.parse(localStorage.getItem("user"));

  const [isEditing, setIsEditing] = useState(false);
 const [name, setName] = useState(user?.nome?.split(" ")[0] || "Utilizador");
  const [bio, setBio] = useState("Apaixonada por culinária saudável e receitas de 15 minutos 🍳");
  const [image, setImage] = useState("/images/tomate.webp");
  const [bannerPic, setBannerPic] = useState("/images/fundo_hero.webp");

  const handleImageChange = (e, type) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        if (type === 'profile') setImage(reader.result);
        if (type === 'banner') setBannerPic(reader.result);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleSave = async () => {
    const updatedData = { name, bio, image, bannerPic };

    try {
      console.log("Dados atualizados do perfil:", updatedData);
      setIsEditing(false);
      alert("Perfil atualizado com sucesso!");
    } catch (error) {
      console.error("Erro ao guardar:", error);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    navigate("/login");
  };

  if (!user) {
    return (
      <main className="min-h-screen flex items-center justify-center bg-tan-200 px-6">
        <div className="bg-white/80 backdrop-blur-md p-8 rounded-3xl shadow-lg text-center max-w-md w-full">
          <h2 className="text-3xl font-bold text-shadow-grey-700 mb-4">Perfil</h2>
          <p className="text-shadow-grey-700 mb-6">Nenhum utilizador autenticado.</p>
          <button
            onClick={() => navigate("/login")}
            className="rounded-full bg-gradient-to-r from-red-500 to-orange-500 py-3 px-6 text-sm font-semibold text-white shadow-lg transition-all hover:opacity-90"
          >
            Ir para Login
          </button>
        </div>
      </main>
    );
  }

  return (
    <main className="relative min-h-screen w-full overflow-hidden bg-tan-200">
      <div className="relative z-10">
        <section className="relative pt-36 pb-24">
          <img
            src="/images/fundo_hero.webp"
            alt="Banner"
            className="w-full absolute top-0 left-0 z-0 h-60 object-cover shadow-md"
          />

          <div className="w-full max-w-7xl mx-auto px-6 md:px-8">
            <div className="absolute top-0 left-0 w-full h-60 z-0 overflow-hidden group">
              <img
                src={bannerPic}
                alt="Banner"
                className="w-full h-full object-cover"
              />

              {isEditing && (
                <label className="absolute inset-0 flex items-center justify-center bg-black/30 backdrop-blur-sm cursor-pointer opacity-0 group-hover:opacity-100 transition-all">
                  <span className="bg-white/20 border border-white/50 text-white px-4 py-2 rounded-full font-bold text-sm">
                    Alterar Capa
                  </span>
                  <input
                    type="file"
                    className="hidden"
                    accept="image/*"
                    onChange={(e) => handleImageChange(e, 'banner')}
                  />
                </label>
              )}
            </div>

            <div className="flex items-center justify-center relative z-10 mb-6">
              <div className="relative group">
                <img
                  src={image}
                  alt="Avatar"
                  className="border-4 border-solid border-white rounded-full object-cover w-32 h-32 shadow-lg transition-transform group-hover:scale-105"
                />

                {isEditing && (
                  <label className="absolute inset-0 flex items-center justify-center bg-black/40 rounded-full cursor-pointer opacity-0 group-hover:opacity-100 transition-all border-2 border-white/50">
                    <span className="text-white text-[10px] font-bold uppercase text-center px-2">
                      Alterar Foto
                    </span>
                    <input
                      type="file"
                      className="hidden"
                      accept="image/*"
                      onChange={(e) => handleImageChange(e, 'profile')}
                    />
                  </label>
                )}
              </div>
            </div>

            <div className="flex flex-col sm:flex-row max-sm:gap-5 items-center justify-between mb-5 relative z-10">
              <ul className="flex items-center gap-5">
                <li>
                  <a href="/" className="flex items-center gap-2 cursor-pointer group">
                    <span className="font-medium text-base leading-7 text-shadow-grey-700 hover:text-orange-500 transition">
                      Home
                    </span>
                  </a>
                </li>
              </ul>

              <div className="flex items-center gap-4 flex-wrap justify-center">
                {isEditing ? (
                  <button
                    onClick={handleSave}
                    className="rounded-full bg-white py-2.5 px-6 text-sm font-bold text-shadow-grey-700 shadow-lg hover:bg-white transition-all"
                  >
                    Guardar
                  </button>
                ) : (
                  <button
                    onClick={() => setIsEditing(true)}
                    className="rounded-full border border-gray-300 bg-white py-2.5 px-5 text-sm font-semibold text-shadow-grey-700 shadow-sm transition-all hover:bg-text-shadow-grey-700"
                  >
                    Editar Perfil
                  </button>
                )}

                <button className="rounded-full bg-gradient-to-r from-red-500 to-orange-500 py-2.5 px-5 text-sm font-semibold text-white shadow-lg transition-all hover:opacity-90">
                  Nova Receita
                </button>

                <button
                  onClick={handleLogout}
                  className="rounded-full bg-gray-800 py-2.5 px-5 text-sm font-semibold text-white shadow-lg transition-all hover:opacity-90"
                >
                  Terminar sessão
                </button>
              </div>
            </div>

            <div className="relative z-10 text-center max-w-2xl mx-auto">
              {isEditing ? (
                <div className="flex flex-col gap-1 mb-6 animate-in fade-in zoom-in duration-300">
                  <input
                    type="text"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    className="bg-white/50 backdrop-blur-sm border-2 border-golden-chestnut-500 rounded-xl py-1 text-center text-shadow-gray-700 focus:border-berry-500 outline-none"
                    placeholder="O teu nome"
                  />
                  <textarea
                    value={bio}
                    onChange={(e) => setBio(e.target.value)}
                    className="bg-white/50 backdrop-blur-sm border-2 border-golden-chestnut-500 rounded-xl text-center text-shadow-gray-700 focus:border-berry-500 outline-none min-h-[80px]"
                    placeholder="A tua bio"
                  />
                </div>
              ) : (
                <>
                  <h3 className="font-bold text-5xl leading-10 text-shadow-grey-700 mb-1">
                    {name}
                  </h3>
                  <p className="font-normal text-sm leading-6 text-shadow-grey-700 mb-2 opacity-80">
                    Perfil pessoal
                  </p>
                  <p className="font-normal text-base leading-7 text-shadow-grey-700 mb-6 italic">
                    "{bio}"
                  </p>
                </>
              )}
            </div>

            <div className="flex items-center justify-center gap-5 relative z-10">
              <div className="bg-white/80 backdrop-blur-sm border border-gray-200 px-6 py-2 rounded-2xl shadow-sm">
                <span className="font-bold text-orange-600">12</span>
                <span className="ml-2 text-gray-600 text-sm">Favoritas</span>
              </div>
              <div className="bg-white/80 backdrop-blur-sm border border-gray-200 px-6 py-2 rounded-2xl shadow-sm">
                <span className="font-bold text-orange-600">5</span>
                <span className="ml-2 text-gray-600 text-sm">Criadas</span>
              </div>
            </div>
          </div>
        </section>

        <section className="max-w-7xl mx-auto px-6 pb-20">
          <div className="border-t border-white/50 pt-10">
            <div className="mt-10 relative z-10 bg-white/30 backdrop-blur-md p-8 rounded-3xl border border-white/20 shadow-sm">
              <div className="flex items-center justify-between mb-6">
                <h4 className="text-lg font-bold text-shadow-grey-700">Conquistas</h4>
                <span className="text-xs font-medium text-golden-chestnut-500 bg-orange-50 px-3 py-1 rounded-full border border-orange-100">
                  4 / 10 Desbloqueadas
                </span>
              </div>

              <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
                <div className="bg-white/60 backdrop-blur-sm p-4 rounded-2xl border border-gray-100 shadow-sm flex flex-col items-center text-center group hover:border-orange-200 transition-all">
                  <div className="w-12 h-12 bg-orange-100 rounded-full flex items-center justify-center mb-3 group-hover:scale-110 transition-transform">
                    <span className="text-2xl">🌱</span>
                  </div>
                  <span className="text-sm font-bold text-shadow-grey-700">Iniciante Saudável</span>
                  <p className="text-[10px] text-shadow-grey-700 mt-1">Criou a primeira receita</p>
                </div>

                <div className="bg-white/60 backdrop-blur-sm p-4 rounded-2xl border border-gray-100 shadow-sm flex flex-col items-center text-center group hover:border-orange-200 transition-all">
                  <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center mb-3 group-hover:scale-110 transition-transform">
                    <span className="text-2xl">♻️</span>
                  </div>
                  <span className="text-sm font-bold text-shadow-grey-700">Zero Desperdício</span>
                  <p className="text-[10px] text-shadow-grey-700 mt-1">Usou sobras em 5 pratos</p>
                </div>

                <div className="bg-white/60 backdrop-blur-sm p-4 rounded-2xl border border-gray-100 shadow-sm flex flex-col items-center text-center group hover:border-orange-200 transition-all">
                  <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center mb-3 group-hover:scale-110 transition-transform">
                    <span className="text-2xl">🔥</span>
                  </div>
                  <span className="text-sm font-bold text-shadow-grey-700">Chef Consistente</span>
                  <p className="text-[10px] text-shadow-grey-700 mt-1">7 dias seguidos</p>
                </div>

                <div className="bg-white/60 backdrop-blur-sm p-4 rounded-2xl border border-gray-100 shadow-sm flex flex-col items-center text-center group hover:border-orange-200 transition-all">
                  <div className="w-12 h-12 bg-yellow-100 rounded-full flex items-center justify-center mb-3 group-hover:scale-110 transition-transform">
                    <span className="text-2xl">⭐</span>
                  </div>
                  <span className="text-sm font-bold text-gray-800">Mestre Rapidez</span>
                  <p className="text-[10px] text-gray-500 mt-1">Receita Avaliada</p>
                </div>
              </div>
            </div>

            <br />

            <h4 className="text-xl font-bold mb-6 text-shadow-grey-700 mt-10">As Minhas Receitas</h4>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="h-64 bg-gray-200/50 backdrop-blur-sm rounded-3xl animate-pulse"></div>
              <div className="h-64 bg-gray-200/50 backdrop-blur-sm rounded-3xl animate-pulse"></div>
              <div className="h-64 bg-gray-200/50 backdrop-blur-sm rounded-3xl animate-pulse"></div>
            </div>
          </div>
        </section>
      </div>
    </main>
  );
};

export default ProfilePage;
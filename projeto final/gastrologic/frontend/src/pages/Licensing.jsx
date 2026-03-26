function Licensing() {
  return (
    <div className="min-h-screen py-16 px-6 lg:px-8 bg-[url('/images/fundo_hero.webp')] bg-cover bg-fixed bg-center">
      <div className="max-w-3xl mx-auto bg-white/80 backdrop-blur-sm p-8 md:p-12 rounded-3xl shadow-sm border border-white/20">
        
        <h1 className="text-4xl font-magneton text-shadow-gray-700 mb-8 border-b pb-4 border-shadow-gray-700">
          Licenciamento
        </h1>

        <section className="space-y-8 text-shadow-gray-700">
          <div>
            <h2 className="text-xl mb-3">Propriedade Intelectual</h2>
            <p className="leading-relaxed">
              Todo o código-fonte, design de interface, algoritmos de recomendação e conteúdos originais do <strong>Gastrologic</strong> são protegidos por direitos de autor. A reprodução total ou parcial é estritamente proibida sem autorização por escrito.
            </p>
          </div>

          <div>
            <h2 className="text-xl mb-3">Software de Terceiros</h2>
            <p className="leading-relaxed text-sm">
              Utilizamos tecnologias Open Source para entregar a melhor experiência. Agradecemos à comunidade de desenvolvedores do <strong>React, Tailwind CSS, e Vite</strong> por disponibilizarem ferramentas sob a licença MIT.
            </p>
          </div>

          <div>
            <h2 className="text-lg mb-2">Uso Comercial</h2>
            <p className="text-sm italic">
              Para parcerias ou licenciamento comercial da nossa tecnologia de gestão nutricional, por favor entre em contacto através da nossa página de contactos.
            </p>
          </div>
        </section>

        <div className="mt-12 pt-8 border-t text-shadow-gray-700 text-center text-shadow-gray-700 text-xs">
          © 2026 Gastrologic - Todos os direitos reservados.
        </div>
      </div>
    </div>
  );
}

export default Licensing;
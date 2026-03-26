function PrivacyPolicy() {
  return (
    <div className="min-h-screen py-16 px-6 lg:px-8 bg-[url('/images/fundo_hero.webp')] bg-cover bg-fixed bg-center">
      
      <div className="max-w-3xl mx-auto bg-white/50 backdrop-blur-sm p-8 md:p-12 rounded-3xl shadow-sm border border-white/20">
        
        <h1 className="text-4xl font-magneton text-shadow-gray-700 mb-8 border-b pb-4 border-gray-100">
          Política de <span className="text-berry-500">Privacidade</span>
        </h1>

        <p className="text-shadow-gray-700 mb-8 leading-relaxed font-medium">
          No Gastrologic, a tua privacidade é a nossa prioridade. Esta aplicação foi desenhada para respeitar o 
          <strong> Regulamento Geral de Proteção de Dados (RGPD)</strong>.
        </p>

        <section className="space-y-8">
          <div>
            <h2 className="text-xl text-shadow-gray-700 mb-3 flex items-center font-semibold">
              <span className="bg-berry-100 text-berry-600 w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm font-bold">1</span>
              Dados Recolhidos
            </h2>
            <ul className="list-disc ml-14 text-shadow-gray-700 space-y-2 font-medium">
              <li><strong>Nome:</strong> Para personalizar a tua experiência.</li>
              <li><strong>Email:</strong> Para identificação da conta.</li>
              <li><strong>Password:</strong> Encriptada.</li>
            </ul>
          </div>

          <div>
            <h2 className="text-xl text-shadow-gray-700 mb-3 flex items-center font-semibold">
              <span className="bg-berry-100 text-berry-600 w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm font-bold">2</span>
              Finalidade
            </h2>
            <p className="ml-11 text-shadow-gray-700 leading-relaxed font-medium">
              Os teus dados são utilizados exclusivamente para gerir a tua conta, guardar as tuas preferências de ingredientes e o teu perfil nutricional.
            </p>
          </div>

          <div>
            <h2 className="text-xl text-shadow-gray-700 mb-3 flex items-center font-semibold">
              <span className="bg-berry-100 text-berry-600 w-8 h-8 rounded-full flex items-center justify-center mr-3 text-sm font-bold">3</span>
              Os Teus Direitos
            </h2>
            <p className="ml-11 text-shadow-gray-700 leading-relaxed font-medium">
              Tens total controlo. Podes aceder, alterar ou eliminar permanentemente os teus dados a qualquer momento através das definições de perfil.
            </p>
          </div>

          <div className="bg-berry-50/50 p-6 rounded-2xl border-l-4 border-berry-500">
            <h2 className="text-lg text-shadow-shadow-gray-700 mb-2 font-semibold">Segurança</h2>
            <p className="text-shadow-gray-700 text-sm italic font-medium leading-relaxed">
              Utilizamos protocolos de encriptação modernos para garantir que a tua informação permanece segura contra acessos não autorizados.
            </p>
          </div>
        </section>

        <div className="mt-12 pt-8 border-t border-shadow-gray-700 text-center">
          <p className="text-sm text-shadow-gray-700 font-medium">
            Última atualização: Março de 2026
          </p>
        </div>
      </div>
    </div>
  );
}

export default PrivacyPolicy;
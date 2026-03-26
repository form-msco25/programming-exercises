import { Link } from 'react-router-dom'; 

function Footer() {
  return (
    <footer className="w-full py-4 bg-tan-200/25"> 
      <div className="w-full mx-auto max-w-screen-xl md:flex md:items-center md:justify-between">
        
        <span className="text-sm text-berry-500 sm:text-center font-medium">
          © 2026 <Link to="/" className="hover:underline">Gastrologic™</Link>. Todos os direitos reservados.
        </span>

        <ul className="flex flex-wrap items-center mt-3 text-sm font-semibold text-berry-500 sm:mt-0">
          <li>
            <Link to="/about" className="hover:underline me-4 md:me-6">Sobre</Link>
          </li>
          <li>
            <Link to="/privacypolicy" className="hover:underline me-4 md:me-6">Políticas de Privacidade</Link>
          </li>
          <li>
            <Link to="/licensing" className="hover:underline me-4 md:me-6">Licenciamento</Link>
          </li>
          <li>
            <Link to="/contactos" className="hover:underline me-4 md:me-6">Contactos</Link>
          </li>
        </ul>
      </div>
    </footer>
  );
}

export default Footer;
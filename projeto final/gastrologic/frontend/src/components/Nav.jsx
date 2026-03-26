import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { isTokenExpired, logoutUser } from "../utils/auth";

function Nav() {
  const token = localStorage.getItem("token");

  const user = token && !isTokenExpired(token)
    ? JSON.parse(localStorage.getItem("user"))
    : null;

  const [isOpen, setIsOpen] = useState(false);
  const navigate = useNavigate();

  const closeMenu = () => setIsOpen(false);

  const handleLogout = () => {
    logoutUser();
    closeMenu();
    navigate("/login");
  };

  return (
    <nav className="bg-white/50 backdrop-blur-md fixed w-full z-50 top-0 start-0 border-b border-gray-100">
      <div className="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto py-2 px-4">
        <Link to="/" onClick={closeMenu} className="flex items-center space-x-3">
          <img
            src="/images/logo.webp"
            className="h-10 w-auto object-contain"
            alt="Logo"
          />
          <span className="self-center text-2xl font-bold whitespace-nowrap text-[--shadow-grey]">
            GastroLogic
          </span>
        </Link>

        <button
          onClick={() => setIsOpen(!isOpen)}
          type="button"
          className="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none"
        >
          <span className="sr-only">Abrir menu</span>
          <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            {isOpen ? (
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12" />
            ) : (
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16m-7 6h7" />
            )}
          </svg>
        </button>

        <div className={`${isOpen ? 'block' : 'hidden'} w-full md:block md:w-auto absolute md:static top-full right-4 mt-2 md:mt-0`}>
          <ul className="flex flex-col md:flex-row items-center font-medium bg-white/100 md:bg-transparent shadow-xl md:shadow-none rounded-2xl p-4 md:p-0 space-y-2 md:space-y-0 md:space-x-8 ml-auto max-w-[260px] md:max-w-none">
            <li>
              <Link to="/" onClick={closeMenu} className="block py-2 px-3 text-[--sage-green] md:p-0">
                Home
              </Link>
            </li>

            <li>
              <Link
                to="/about"
                onClick={closeMenu}
                className="block py-2 px-3 text-[--shadow-grey] rounded hover:text-[--sage-green] md:p-0 transition-colors"
              >
                Sobre
              </Link>
            </li>

            {user && (
              <>
                <li className="text-[--shadow-grey] text-sm px-3">
                  Olá, {user.nome?.split(" ")[0]}
                </li>
                <li>
                  <Link
                    to="/profile"
                    onClick={closeMenu}
                    className="block py-2 px-3 text-[--shadow-grey] rounded hover:text-[--sage-green] md:p-0 transition-colors"
                  >
                    Perfil
                  </Link>
                </li>
              </>
            )}

            {!user ? (
              <li className="w-full md:w-auto">
                <Link
                  to="/login"
                  onClick={closeMenu}
                  className="block md:inline-block py-2 px-3 text-[--dusty-mauve] hover:bg-[--dusty-mauve]/10 rounded-full transition-all text-center"
                >
                  Log In
                </Link>
              </li>
            ) : (
              <li className="w-full md:w-auto">
                <button
                  onClick={handleLogout}
                  className="block md:inline-block py-2 px-3 text-[--dusty-mauve] hover:bg-[--dusty-mauve]/10 rounded-full transition-all text-center w-full"
                >
                  Terminar Sessão
                </button>
              </li>
            )}
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Nav;
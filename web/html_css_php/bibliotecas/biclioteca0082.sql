-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 22-Set-2025 às 18:51
-- Versão do servidor: 10.4.6-MariaDB
-- versão do PHP: 7.2.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `biclioteca0082`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `manuais`
--

CREATE TABLE `manuais` (
  `id` int(11) NOT NULL,
  `titulo` varchar(40) NOT NULL,
  `numpag` varchar(11) DEFAULT '0',
  `textdescr` mediumtext DEFAULT NULL,
  `pesokb` varchar(6) NOT NULL DEFAULT '0',
  `autor` varchar(20) DEFAULT 'Desconhecido'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `manuais`
--

INSERT INTO `manuais` (`id`, `titulo`, `numpag`, `textdescr`, `pesokb`, `autor`) VALUES
(1, 'SQL', '50+10', 'Manual simples com 50 páginas de conteúdo teórico +10 páginas de exercícios simples.', '0', 'Desconhecido'),
(2, 'Linux para todos', '350', 'Manual Simples, com demostrações prática para gerir o seu servidor e instalar diferentes tipos de serviços', '35000', 'Rui Monteiro'),
(3, '', '300', 'Conhecimentos bÃ¡sicos na linguagem C', '125', 'AnÃ³nimo');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `manuais`
--
ALTER TABLE `manuais`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `manuais`
--
ALTER TABLE `manuais`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

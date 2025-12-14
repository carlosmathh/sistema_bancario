# 🏦 Sistema Bancário em Python (POO)

Este projeto simula um sistema bancário simples, desenvolvido em **Python**, com foco na prática de **Programação Orientada a Objetos (POO)** e na aplicação de regras de negócio próximas ao mundo real.

O sistema modela **clientes**, **contas bancárias** e um **banco**, centralizando validações como autenticação, saque, depósito e limite de crédito.

---

## 🎯 Objetivo do Projeto

- Consolidar fundamentos de **POO em Python**
- Aplicar conceitos como **abstração, herança, polimorfismo, encapsulamento e agregação**
- Modelar regras de negócio de forma clara e organizada
- Escrever código mais próximo de padrões utilizados no mercado

---

## 🧠 Conceitos Aplicados

- Classes Abstratas (`ABC`)
- Herança e Polimorfismo
- Encapsulamento com `@property`
- Agregação entre objetos
- Regras de negócio e tratamento de exceções
- Código organizado e orientado ao domínio do problema

---

## 🏗️ Estrutura das Classes

### 🔹 Account (Classe Abstrata)
- Representa uma conta bancária genérica.
- Define atributos comuns: agência, número da conta e saldo.
- Centraliza validações básicas de saque.
- Obriga subclasses a implementarem o método `withdraw`.

---

### 🔹 Person (Classe Abstrata)
- Representa uma pessoa no sistema.
- Possui atributos básicos como nome e idade.
- Serve como base para a classe `Client`.

---

### 🔹 Client
- Representa o cliente do banco.
- Herda de `Person`.
- Possui uma conta associada (agregação com `Account`).
- Utiliza **encapsulamento** com `@property` para proteger dados sensíveis.

---

### 🔹 Bank
- Centraliza as **regras de negócio** do sistema.
- Agrega clientes e contas.
- Responsável pela **autenticação**, validando:
  - Se o cliente pertence ao banco
  - Se a conta pertence ao banco
  - Se a agência é válida
- Atua como intermediário entre cliente e conta para saque e depósito.

---

### 🔹 CurrentAccount
- Especialização da classe `Account`.
- Representa uma **conta corrente**.
- Possui **limite de crédito**.
- Permite saque utilizando saldo + limite.
- Aplica validações para evitar uso indevido do crédito.

---

### 🔹 SavingsAccount
- Especialização da classe `Account`.
- Representa uma **conta poupança**.
- Permite saque apenas se houver saldo suficiente.
- Não possui limite de crédito.

---

## 🌍 Padrão de Código

O código foi escrito em **inglês**, seguindo o padrão utilizado no mercado de tecnologia, facilitando a leitura em ambientes profissionais e equipes internacionais.

---

## 🚀 Próximos Passos

- Implementar um **menu interativo** no terminal
- Melhorar a experiência de uso do sistema
- Adicionar novos tipos de contas
- Evoluir validações e regras de negócio

---

O projeto possui uma interface simples
em terminal (menu.py), separada da lógica de negócio, 
seguindo boas práticas de organização e responsabilidade única (SRP).

---

## 📌 Status do Projeto

🟢 Em desenvolvimento — versão inicial focada em POO concluída.

---

## 👨‍💻 Autor

Carlos Matheus  
Estudante de Análise e Desenvolvimento de Sistemas  
Em transição para a área de Tecnologia

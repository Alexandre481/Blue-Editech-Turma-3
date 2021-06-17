{https://github.com/Alexandre481/Blue-Editech-Turma-3-C6.git
      "cell_type": "markdown",
      "metadata": {
        "id": "ksvbOd2t18Sl"
      },
      "source": [
        "###                        Projeto 01 – Detetive\n",
        "\n",
        "Esse projeto tem a finalidade de fixar os conhecimentos de Variáveis, Print, Input e Condicionais, para isso crie um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:\n",
        "\n",
        "\"Você telefonou para a vítima?\"\n",
        "\n",
        "\" Você esteve no local do crime?\"\n",
        "\n",
        "\" Você mora perto da vítima?\"\n",
        "\n",
        "\" Você devia para a vítima?\"\n",
        "\n",
        "\" Você já trabalhou com a vítima?\"\n",
        "\n",
        "O programa deve, no final, emitir uma classificação sobre a participação da pessoa no crime.\n",
        "\n",
        "Se a pessoa responder positivamente a:\n",
        "\n",
        "\n",
        "\n",
        " 2 questões ela deve ser classificada como \"Suspeita\",\n",
        "\n",
        "  Entre 3 e 4 como \"Cúmplice\"\n",
        "  5 como \"Assassino\".\n",
        "  Caso contrário, ele será classificado como \"Inocente\".\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_jU9Zler-TPA",
        "outputId": "1d81cee3-56b4-48b1-cda2-b3798bac1c15"
      },
      "source": [
        "print (\"          Projeto Detetive          \\n \")\n",
        "print(\"Por favor,digite Sim ou Não,para as perguntas abaixo:\\n\")\n",
        "varTel=input(\"Você telefonou para a vítima?  \").upper()\n",
        "varLoc=input(\"Você esteve no local do crime?  \").upper()\n",
        "varMor=input(\"Você mora perto da vítima?  \").upper()\n",
        "varDev=input(\"Você devia para a vítima?  \").upper()\n",
        "varTra=input(\"Você já trabalhou com a vítima?   \").upper()\n",
        "varC=varTel.count(\"SIM\")+varLoc.count(\"SIM\")+varMor.count(\"SIM\")+varDev.count(\"SIM\")+varTra.count(\"SIM\")\n",
        "if varC ==2:\n",
        "  print(\"Esta pessoa é considerada suspeita.\\n\")\n",
        "else:\n",
        "  if varC  ==3:\n",
        "    print(\"Esta pessoa é considerada Cumplíce.\\n\")\n",
        "if varC ==4:\n",
        "   print(\"Esta pessoa é considerada cumplice.\\n\")\n",
        "else:\n",
        "  if varC==5:\n",
        "    print(\"Esta pessoa é considerada assassina.\\n\")\n",
        "if varC <2:\n",
        "  print(\"Esta pessoa é inocente.\\n\")\n"
      ],
      "execution_count": 79,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "          Projeto Detetive          \n",
            " \n",
            "Por favor,digite Sim ou Não,para as perguntas abaixo:\n",
            "\n",
            "Você telefonou para a vítima?  não\n",
            "Você esteve no local do crime?  sim\n",
            "Você mora perto da vítima?  não\n",
            "Você devia para a vítima?  não\n",
            "Você já trabalhou com a vítima?   sim\n",
            "Esta pessoa é considerada suspeita.\n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
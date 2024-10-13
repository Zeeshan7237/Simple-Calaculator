{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMx1mcwwGYHjQB3EcwjOxPz",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Zeeshan7237/Simple-Calaculator/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "P4hoXoe-Or1h",
        "outputId": "24d39263-f579-4b31-df34-318dd6650141"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Select operation:\n",
            "1. Add\n",
            "2. Subtract\n",
            "3. Multiply\n",
            "4. Divide\n",
            "Enter choice (1/2/3/4): 1\n",
            "Enter first number: 29\n",
            "Enter second number: 29\n",
            "29.0 + 29.0 = 58.0\n"
          ]
        }
      ],
      "source": [
        "import streamlit as st\n",
        "\n",
        "# Simple calculator functions\n",
        "def add(x, y):\n",
        "    return x + y\n",
        "\n",
        "def subtract(x, y):\n",
        "    return x - y\n",
        "\n",
        "def multiply(x, y):\n",
        "    return x * y\n",
        "\n",
        "def divide(x, y):\n",
        "    if y != 0:\n",
        "        return x / y\n",
        "    else:\n",
        "        return \"Error! Division by zero.\"\n",
        "\n",
        "# Streamlit UI\n",
        "st.title(\"Simple Calculator\")\n",
        "\n",
        "# Select operation\n",
        "operation = st.selectbox(\"Select operation\", [\"Add\", \"Subtract\", \"Multiply\", \"Divide\"])\n",
        "\n",
        "# Input numbers\n",
        "num1 = st.number_input(\"Enter first number\", value=0.0)\n",
        "num2 = st.number_input(\"Enter second number\", value=0.0)\n",
        "\n",
        "# Perform calculation based on selected operation\n",
        "if st.button(\"Calculate\"):\n",
        "    if operation == \"Add\":\n",
        "        result = add(num1, num2)\n",
        "    elif operation == \"Subtract\":\n",
        "        result = subtract(num1, num2)\n",
        "    elif operation == \"Multiply\":\n",
        "        result = multiply(num1, num2)\n",
        "    elif operation == \"Divide\":\n",
        "        result = divide(num1, num2)\n",
        "\n",
        "    st.write(f\"The result is: {result}\")\n"
      ]
    }
  ]
}
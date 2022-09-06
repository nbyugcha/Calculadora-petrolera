const { createApp } = Vue;

createApp({
  data() {
    return {
      resultadoConversion: '',
      data: {
        tipo: "volumen",
        cantidad: undefined,
      },
    };
  },
  computed: {
    unidades() {
      if (this.data.tipo === "volumen") {
        return {
          m3: "Metro cúbico",
          bl: "Barril",
          ft3: "Pie cúbico",
          gl: "Galón",
          lt: "Litro",
        };
      } else {
        return {
          kelvin: "Kelvin",
          celsius: "Grado celsius",
          fahrenheit: "Grado fahrenheit",
          rankine: "Grado rankine",
        };
      }
    },
  },
  methods: {
    enviarFormulario() {
      this.resultadoConversion = ''
      fetch("/calculadora", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.data),
      })
        .then((response) => response.json())
        .then((data) => {
          this.resultadoConversion = data.resultado
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
  },
}).mount("#app");

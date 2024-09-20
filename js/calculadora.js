const appliances = {
    sala: ["TV", "Ventilador", "Lâmpada", "Home Theater", "Computador"],
    cozinha: ["Geladeira", "Microondas", "Liquidificador", "Fogão Elétrico", "Forno Elétrico"],
    quarto: ["Ar-condicionado", "Ventilador", "Lâmpada", "Carregador de Celular", "TV"],
    banheiro: ["Chuveiro Elétrico", "Secador de Cabelo", "Máquina de Barbear", "Lâmpada"] // Eletrodomésticos do banheiro
};

// Atualiza a lista de aparelhos com base no ambiente selecionado
function updateAppliances() {
    const room = document.getElementById("room").value;
    const applianceSelect = document.getElementById("appliance");
    
    // Limpa as opções anteriores
    applianceSelect.innerHTML = "";

    // Adiciona novas opções com base no ambiente selecionado
    appliances[room].forEach(appliance => {
        const option = document.createElement("option");
        option.value = appliance;
        option.text = appliance;
        applianceSelect.add(option);
    });
}

// Calcula o consumo de energia e o custo
function calculateEnergy() {
    const power = parseFloat(document.getElementById("power").value);
    const time = parseFloat(document.getElementById("time").value);
    const cost = parseFloat(document.getElementById("cost").value);
    const tariff = document.getElementById("tariff").value;

    let tariffMultiplier = 0;
    if (tariff === "amarela") tariffMultiplier = 0.01874;
    else if (tariff === "vermelha1") tariffMultiplier = 0.03971;
    else if (tariff === "vermelha2") tariffMultiplier = 0.09492;

    if (power && time && cost) {
        const energy = (power * time) / 1000; // kWh
        const totalCost = energy * (cost + tariffMultiplier);

        document.getElementById("result").innerHTML = `
            Consumo de Energia: ${energy.toFixed(2)} kWh<br>
            Custo Aproximado: R$ ${totalCost.toFixed(2)}
        `;
    } else {
        document.getElementById("result").innerHTML = "Por favor, preencha todos os campos.";
    }
}


// Inicializa os aparelhos para o ambiente padrão (sala)
updateAppliances();

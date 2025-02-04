document.addEventListener("DOMContentLoaded", function () {
    const formMateria = document.getElementById("formMateria");
    const nomeMateria = document.getElementById("nomeMateria");
    const listaMaterias = document.getElementById("listaMaterias");
    const selecaoMateria = document.getElementById("selecaoMateria");

    const formAtividade = document.getElementById("formAtividade");
    const conteudo = document.getElementById("conteudo");
    const status = document.getElementById("status");
    const prazo = document.getElementById("prazo");
    const listaAtividades = document.getElementById("listaAtividades");

    formMateria.addEventListener("submit", function (event) {
        event.preventDefault();
        const materiaTexto = nomeMateria.value.trim();
        if (materiaTexto !== "") {
            // Adicionar à lista de matérias
            const materiaItem = document.createElement("li");
            materiaItem.textContent = materiaTexto;
            listaMaterias.appendChild(materiaItem);

            // Adicionar ao seletor de matérias
            const option = document.createElement("option");
            option.value = materiaTexto;
            option.textContent = materiaTexto;
            selecaoMateria.appendChild(option);

            nomeMateria.value = "";
        }
    });

    formAtividade.addEventListener("submit", function (event) {
        event.preventDefault();
        const materiaSelecionada = selecaoMateria.value;
        const conteudoTexto = conteudo.value.trim();
        const statusTexto = status.value.trim();
        const prazoTexto = prazo.value;

        if (materiaSelecionada && conteudoTexto && statusTexto && prazoTexto) {
            // Criar card de atividade
            const atividadeDiv = document.createElement("div");
            atividadeDiv.classList.add("atividade");
            atividadeDiv.innerHTML = `
                <p><strong>Matéria:</strong> ${materiaSelecionada}</p>
                <p><strong>Conteúdo:</strong> ${conteudoTexto}</p>
                <p><strong>Status:</strong> ${statusTexto}</p>
                <p><strong>Prazo:</strong> ${prazoTexto}</p>
            `;

            listaAtividades.appendChild(atividadeDiv);

            // Limpar campos
            conteudo.value = "";
            status.value = "";
            prazo.value = "";
        }
    });
});
document.getElementById("materiaForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let materiaInput = document.getElementById("materia");
    let materiaNome = materiaInput.value.trim();

    if (materiaNome !== "") {
        let lista = document.getElementById("listaMaterias");
        let novaMateria = document.createElement("li");
        novaMateria.textContent = materiaNome;
        lista.appendChild(novaMateria);
        
        materiaInput.value = ""; // Limpa o campo de entrada
    }
});
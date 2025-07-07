document.addEventListener("DOMContentLoaded", function () {
    const mensagens = document.querySelectorAll(".mensagem-sucesso");

    mensagens.forEach(function (msg) {
        // Clique no X
        msg.querySelector(".fechar-msg").onclick = function () {
            msg.classList.add("ocultar");
            setTimeout(() => msg.style.display = "none", 600);
        };

        // Auto esconder após 5s
        setTimeout(function () {
            msg.classList.add("ocultar");
            setTimeout(() => msg.style.display = "none", 600);
        }, 5000);
    });
});
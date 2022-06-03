function confirmarAdCat(){
    alert('Categoria salva com sucesso')
}

(function(){
    const btnexcat = document.querySelectorAll(".exclusaocat")

    btnexcat.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacao = confirm("Tem certeza que quer excluir?");
            if (!confirmacao){
                e.preventDefault();
            }
        });
    })
})();

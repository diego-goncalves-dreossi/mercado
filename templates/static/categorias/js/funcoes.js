function confirmarAdCat(){
    alert('Categoria salva com sucesso')
}

(function(){
    const btnexcat = document.querySelectorAll(".exclusao")

    btnexcat.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacao = confirm("Tem certeza que quer excluir categoria?");
            if (!confirmacao){
                e.preventDefault();
            }
        });
    })
})();
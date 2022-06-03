function confirmarAdForn(){
    alert('Fornecedor salvo com sucesso')
}

(function(){
    const btnexfn = document.querySelectorAll(".exclusao")

    btnexfn.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacao = confirm("Tem certeza que quer excluir fornecedor?");
            if (!confirmacao){
                e.preventDefault();
            }
        });
    })
})();

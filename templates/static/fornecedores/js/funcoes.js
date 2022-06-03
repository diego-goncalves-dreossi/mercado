function confirmarAd(){
    alert('Salvo com sucesso')
}

function confirmarEd(){
    alert('Editado com sucesso')
}

function confirmarEx(){
    alert('Excluido com sucesso')
}

(function(){
    const btnexfn = document.querySelectorAll(".efn")

    btnexfn.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacao = confirm("Tem certeza que quer excluir fornecedor?");
            if (!confirmacao){
                e.preventDefault();
            }
        });
    })
})();

(function(){
    const btnadfn = document.querySelectorAll(".afn")

    btnadfn.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacao = confirm("Adicionar fornecedor?");
            if (!confirmacao){
                e.preventDefault();
            }
        });
    })
})();

(function(){
    const btnedfn = document.querySelectorAll(".efn")

    btnedfn.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacao = confirm("Editar fornecedor?");
            if (!confirmacao){
                e.preventDefault();
            }
        });
    })
})();



(function(){
    const btnai = document.querySelectorAll(".afnimg")

    btnai.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacao = confirm("Alterar imagem de fornecedor?");
            if (!confirmacao){
                e.preventDefault();
            }
        });
    })
})();
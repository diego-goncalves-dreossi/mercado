function confirmarAd(){
    alert('Salvo com sucesso')
}

function confirmarEd(){
    alert('Editado com sucesso')
}

function confirmarEx(){
    alert('Excluido com sucesso')
}

function confirmarAltImg(){
    alert('Logo do Fornecedor alterado com sucesso');
}


(function(){
    const btnexfn = document.querySelectorAll(".epr")

    btnexfn.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacao = confirm("Tem certeza que quer excluir produto?");
            if (!confirmacao){
                e.preventDefault();
            }
        });
    })
})();

(function(){
    const btnadpr = document.querySelectorAll(".apr")

    btnadpr.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacao = confirm("Adicionar produto?");
            if (!confirmacao){
                e.preventDefault();
            }
        });
    })
})();



(function(){
    const btnedpr = document.querySelectorAll(".edpr")

    btnedpr.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacao = confirm("Editar produto?");
            if (!confirmacao){
                e.preventDefault();
            }
        });
    })
})();

(function(){
    const btnai = document.querySelectorAll(".aprimg")

    btnai.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacao = confirm("Alterar imagem de produto?");
            if (!confirmacao){
                e.preventDefault();
            }
        });
    })
})();

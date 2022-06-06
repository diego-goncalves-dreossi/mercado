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
    const btnexcat = document.querySelectorAll(".ecat")

    btnexcat.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacao = confirm("Tem certeza que quer excluir pedido?");
            if (!confirmacao){
                e.preventDefault();
            }
        });
    })
})();

(function(){
    const btnacat = document.querySelectorAll(".acat")

    btnacat.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacao = confirm("Tem certeza que quer adicionar pedido?");
            if (!confirmacao){
                e.preventDefault();
            }
        });
    })
})();

(function(){
    const btnedcat = document.querySelectorAll(".edcat")

    btnedcat.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacao = confirm("Tem certeza que quer editar pedido?");
            if (!confirmacao){
                e.preventDefault();
            }
        });
    })
})();


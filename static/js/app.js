new Vue(
    {
        el: '#movies_app',
        data: {
            movies:[]
        },
        created: function () {
            const vm = this;
            axios.get('/api/movies/')
                .then(function (response){
                    vm.movies = response.data
                })
        }
    }
)
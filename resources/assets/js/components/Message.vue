<template>
    <div class="container">
        <div class="row">
            <div class="col-md-8 col-md-offset-2">
                <div class="panel panel-default" v-for="message in messages">
                <div class="panel-heading"><strong>{{message.user.name}}</strong></div>
                <div class="panel-body"><p>{{message.message}}</p></div>  
            </div>
        </div>
        </div>
    </div>
</template>
<script>
export default {
    props: ['message'],
    mounted(){
        console.log(this.message);
    },
    data(){
    return {
        message: 'whaaaaaaaaaaaaaaaaaaaaaaaaaaat',
        user: 'whoooo',
    }
}
}
</script>
<style scoped>
.panel{
    margin-bottom: 0;
}
</style>

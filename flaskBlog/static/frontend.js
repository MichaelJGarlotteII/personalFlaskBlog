function upvote_post(){
    console.log('upvoting post')
    $.post("http://localhost:5000/api/post/"+post_id+"/upvote", function(data){
        alert('post upvoted!');
        console.log('getting upvotes')
        $.get("http://localhost:5000/api/post/"+post_id+"/upvote", function(data) {
            console.log(data.upvotes)
            $("#post-upvotes").text(data.upvotes)
        });
        
    })
}
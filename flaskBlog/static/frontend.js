function upvote_post(){
    console.log('upvoting post')
    $.post("http://michaeljgarlotteii.com:5000/api/post/"+post_id+"/upvote", function(data){
        console.log('getting upvotes')
        $.get("http://michaeljgarlotteii:5000/api/post/"+post_id+"/upvote", function(data) {
            console.log(data.upvotes)
            $("#post-upvotes").text(data.upvotes)
        });
        
    })
}
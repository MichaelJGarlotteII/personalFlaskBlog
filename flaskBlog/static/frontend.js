function vote_on_post(is_upvote){
    console.log('voting on post. is upvote?:', is_upvote);
    $.post("http://michaeljgarlotteii:5000/api/post/"+post_id+"/"+is_upvote, function(data){
        console.log('getting upvotes')
        $.get("http://michaeljgarlotteii:5000/api/post/"+post_id+"/"+is_upvote, function(data) {
            console.log(data.vote_count);
            if(is_upvote){
                $("#post-upvotes").text(data.vote_count);
            } else {
                $("#post-downvotes").text(data.vote_count);
            }
            
        });
        
    })
}
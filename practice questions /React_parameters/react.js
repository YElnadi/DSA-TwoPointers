const review = {
    id: 1,
    userId: 2,
    movie: 'Star War',
    comment: 'It was good',
    review: 5
}

const user = {
    id: 2,
    fname: 'Yas',
    lname: 'Elnadi'
}

const printReviewUser = ({userId:id})=>{
    const user = fetchUserId(id)
    console.log(`${user.fname} ${user.lname}`)
    
}

const printReview = ({movie, comment, rating})=>{
    console.log(`watched ${movie}`);
    console.log(`Gave it ${rating} stars!`);
    console.log(`${comment}`);
}


printReviewUser(review)

printReview(review)
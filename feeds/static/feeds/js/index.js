const onClickLikeButton = async (feedId) => {
    const feedLikeButton = document.getElementById(`${feedId}-like-button`);
    const response = await axios.get(`/feeds/${feedId}/like/`);
    feedLikeButton.innerHTML = `${response.data.feedLikeCount} Likes`
}
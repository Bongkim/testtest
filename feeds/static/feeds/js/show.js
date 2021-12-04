axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

const onAddComment = async (feedId) => {
    const commentInputElement = document.getElementById("comment-input");
    console.log(commentInputElement.value)
    if (commentInputElement.value) {
      // axios로 보내줄 data Form을 만들어 줍니다.
      let data = new FormData();
      // content라는 key를 만들고, comment input 값을 적어줍니다.
      data.append("content", commentInputElement.value);
          // aixos 요청에 의한 응답을 받을 때까지 기다렷다가 response에 할당해준다.
      const response = await axios.post(`/feeds/${feedId}/comments/`, data);
        // 해당 값을 출력해 본다. async await가 없으면 아래 console.log가 에러가 난다.
      console.log(response.data);
  
      const commentList = document.getElementById("comment-list");
      commentList.innerHTML = commentList.innerHTML + `
        <p>
          ${response.data.content}
          <a href="/feeds/${feedId}/comments/${response.data.id}/like/">
            0 Likes
          </a>
          <a href="/feeds/${feedId}/comments/${response.data.id}/delete/">댓글 삭제</a>
        </p>
      `
    }
  }
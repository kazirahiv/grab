

export default function ValidateYouTubeUrl(url: string): boolean {
    if (url !== undefined || url !== "") {
      // eslint-disable-next-line
      var regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=|\?v=)([^#\&\?]*).*/;
      // eslint-disable-next-line
      var match = url.match(regExp);
      if (match && match[2].length === 11) {
        return true;
      } else {
        return false;
      }
    }
    return false;
  }
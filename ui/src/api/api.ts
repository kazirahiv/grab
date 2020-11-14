import axios from "axios";
import { ApiRoutes } from "../common/routes";


export async function PrepareDownload(url: string, onlyAudio: boolean) {
    const result = await axios
    .post(ApiRoutes.PrepareDownload, {
      url: url,
      onlyAudio: onlyAudio,
    })
    .then((response) => response.data)
    .catch((error) => error.message);
    return result;
  }

  export  function GetFileDownloadUrl(filePath: string) : string {
    const url : string  = ApiRoutes.Download+"?path=" + filePath;
    return url;
  }


  export async function SearchVideo(identifier: string) {
    const result = await axios.get(ApiRoutes.SearchVideo, {
      params: {
        search: identifier
      }
    })
    .then((response) => response.data)
    .catch((error) => error.message);
    return result;
  }


  export async function Download(url : string)
  {
    // const urlConstruct = "https://www.youtube.com/watch?v=" + url;
    axios({
      url: 'http://localhost:5000/static/example.pdf',
      method: 'GET',
      responseType: 'blob', // important
    }).then((response) => {
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'file.pdf');
      document.body.appendChild(link);
      link.click();
    });
  }


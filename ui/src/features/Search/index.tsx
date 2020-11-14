import React from "react";
import { DownloadedCard } from "./Components/DownloadedCard";
import { PrepareDownload, GetFileDownloadUrl } from "../../api/api";
import ValidateYouTubeUrl from "../../helpers/YoutubeUrlValidator";
import { StaleCard } from "./Components/StaleCard";
import { DownloadingCard } from "./Components/DownloadingCard";
import { InvalidUrlCard } from "./Components/InvalidURLCard";

let downloadLink = "";

const onChangeValueHandler = (link: string) => {
  downloadLink = link;
};

export default function SearchForm() {
  const [data, setData] = React.useState("stale");
  const [fileName, setFileName] = React.useState("");
  const [fileUrl, setFileUrl] = React.useState("");
  const [backdropOpen, setBackdrop] = React.useState(false);

  const prepareDownload = () => {
    PrepareDownload(downloadLink, true)
      .then((result) => {
        setData("downloaded");
        setFileName(result.fileName);
        setFileUrl(GetFileDownloadUrl(result.filePath));
      })
      .catch((err) => console.log(err));
  };

  const download = () => {
    if (!backdropOpen) {
      setData("initiated");
      setBackdrop(!false);
    }
    console.log(downloadLink);
    if (ValidateYouTubeUrl(downloadLink)) {
      prepareDownload();
    } else {
      setData("invalid");
    }
  };

  if (data === "stale") {
    return (
      <StaleCard
        OnChangeValueHandler={onChangeValueHandler}
        Download={download}
      />
    );
  } else if (data === "initiated") {
    return <DownloadingCard />;
  } else if (data === "downloaded") {
    return <DownloadedCard name={fileName} url={fileUrl} />;
  } else if (data === "invalid") {
    return <InvalidUrlCard />;
  } else {
    return <div></div>;
  }
}

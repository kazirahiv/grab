import React, { useEffect } from "react";
import TextField from "@material-ui/core/TextField";
import { SearchVideo } from "../../../api/api";
import Autocomplete from "@material-ui/lab/Autocomplete";
import SearchDownloadCard from "./SearchDownloadCard";

export default function ItemSearchAutocomplete(props: any) {
  const [searchedData, setSeachedData] = React.useState([]);
  const [data, setDataValue] = React.useState("");
  const [previousData, setPreviousDataValue] = React.useState("");
  const { onChangeValue, download } = props;

  const updateData = (e: any) => {
    setDataValue(e.target.value);
  };

  useEffect(() => {
    onChangeValue(data);
    const delayDebounceFn = setTimeout(() => {
      if (previousData !== data) {
        SearchVideo(data)
          .then((result) => {
            setPreviousDataValue(data);
            setSeachedData(result);
          })
          .catch((err) => console.log(err));
      }
    }, 3000);
    return () => clearTimeout(delayDebounceFn);
  });

  const searchedItemSelectCallback = (url: string) => {
    const urlConstruct = "https://www.youtube.com/watch?v=" + url;
    console.log("here" + urlConstruct);
    onChangeValue(urlConstruct);
    download();
  };

  return (
    <React.Fragment>
      <Autocomplete
        id="free-solo-demo"
        freeSolo
        options={
          Array.isArray(searchedData)
            ? searchedData.map((option: any) => option)
            : []
        }
        onChange={(event, newValue: any) => {
          if (newValue != null) {
            setDataValue(newValue.title);
          }
        }}
        getOptionLabel={(option) => option.title}
        renderOption={(option) => {
          return (
            <SearchDownloadCard
              callback={searchedItemSelectCallback}
              url={option.link}
              name={option.title}
              thumbnail={option.thumbnail}
            />
          );
        }}
        renderInput={(params) => (
          <TextField
            {...params}
            label="Search Here"
            margin="normal"
            variant="outlined"
            onChange={updateData}
          />
        )}
      />
    </React.Fragment>
  );
}

import React from "react";
import Button from "@material-ui/core/Button";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import CardMedia from "@material-ui/core/CardMedia";
import SaveIcon from "@material-ui/icons/Save";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";

type FileInfo = {
  name: string;
  url: string;
};

const useStyles = makeStyles(() => ({
  details: {
    display: "flex",
    flexDirection: "column",
  },
  content: {
    flex: "1 0",
  },
  cover: {
    padding: "100px",
    width: "100%",
    height: "auto",
  },
  root: {
    marginTop: 60,
    display: "flex",
  },
  button: {
    width: 150,
    marginTop: 20,
  },
}));

export function DownloadedCard({ name, url }: FileInfo) {
  const classes = useStyles();
  return (
    <Card className={classes.root}>
      <div className={classes.details}>
        <CardContent className={classes.content}>
          <Typography component="h5" variant="h5">
            Done !
          </Typography>
          <Typography variant="subtitle1" color="textSecondary">
            File - {name} by clicking below ....
          </Typography>
          <a href={url} download={name}>
            <Button
              variant="outlined"
              color="primary"
              size="small"
              className={classes.button}
              startIcon={<SaveIcon />}
            >
              Save
            </Button>
          </a>
        </CardContent>
      </div>
      <CardMedia
        className={classes.cover}
        image="https://icons.iconarchive.com/icons/janosch500/tropical-waters-folders/512/Downloads-icon.png"
        title="Download Media"
      />
    </Card>
  );
}

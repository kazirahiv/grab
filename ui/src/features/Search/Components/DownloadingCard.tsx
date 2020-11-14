import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import CardMedia from "@material-ui/core/CardMedia";
import Typography from "@material-ui/core/Typography";
import CircularProgress from "@material-ui/core/CircularProgress";

const downloadingCardUseStyles = makeStyles((theme) => ({
  details: {
    display: "flex",
    flexDirection: "column",
  },
  content: {
    flex: "1 0",
  },
  root: {
    marginTop: 60,
    display: "flex",
  },
  cover: {
    padding: "100px",
    width: "100%",
    height: "auto",
  },
}));

export function DownloadingCard() {
  const classes = downloadingCardUseStyles();
  return (
    <Card className={classes.root}>
      <div className={classes.details}>
        <CardContent className={classes.content}>
          <Typography component="h5" variant="h5">
            Getting !
          </Typography>
          <Typography variant="subtitle1" color="textSecondary">
            Almost there, getting your content from youtube{" "}
            <CircularProgress color="inherit" />
          </Typography>
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

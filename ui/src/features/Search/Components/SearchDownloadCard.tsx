import React from "react";
import Button from "@material-ui/core/Button";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import CardMedia from "@material-ui/core/CardMedia";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core";

type VideoInfo = {
  name: string;
  url: string;
  thumbnail: string;
  callback: any;
};

const useStyles = makeStyles((theme) => ({
  form: {
    width: "100%",
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
  root: {
    display: "flex",
    width: "100%",
    height: 150,
  },
  details: {
    display: "flex",
    flexDirection: "column",
  },
  content: {
    overflow: "hidden",
    width: 200,
    height: 100,
    textOverflow: "ellipsis",
  },
  cover: {
    width: 150,
  },
  controls: {
    display: "flex",
    alignItems: "center",
    paddingLeft: theme.spacing(1),
    paddingBottom: theme.spacing(1),
  },
}));

export default function SearchDownloadCard({
  name,
  url,
  thumbnail,
  callback,
}: VideoInfo) {
  const classes = useStyles();
  return (
    <Card className={classes.root}>
      <div className={classes.details}>
        <CardContent className={classes.content}>
          <Typography variant="body2" gutterBottom>
            {name}
          </Typography>
        </CardContent>
        <div className={classes.controls}>
          <Button
            onClick={() => {
              callback(url);
            }}
            variant="contained"
            color="primary"
            disableElevation
          >
            Download
          </Button>
        </div>
      </div>
      <CardMedia className={classes.cover} image={thumbnail} title={name} />
    </Card>
  );
}

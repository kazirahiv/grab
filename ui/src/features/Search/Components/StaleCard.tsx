import React from "react";
import Link from "@material-ui/core/Link";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import { makeStyles } from "@material-ui/core/styles";
import ItemSearchAutocomplete from "./ItemSearchAutocomplete";

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

type StaleCardProp = {
  OnChangeValueHandler: any;
  Download: any;
};

export function StaleCard({ OnChangeValueHandler, Download }: StaleCardProp) {
  const classes = useStyles();
  return (
    <div className={classes.form}>
      <ItemSearchAutocomplete
        fullWidth
        download={Download}
        onChangeValue={OnChangeValueHandler}
      />
      <Button
        type="submit"
        fullWidth
        variant="contained"
        color="primary"
        style={{ marginTop: 8 }}
        className={classes.submit}
        onClick={Download}
      >
        Download
      </Button>
      <Grid container>
        <Grid item>
          <Link href="#" variant="body2">
            {"Give a star on Github"}
          </Link>
        </Grid>
      </Grid>
    </div>
  );
}

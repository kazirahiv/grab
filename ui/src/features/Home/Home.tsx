import React from "react";
import CssBaseline from "@material-ui/core/CssBaseline";
import Box from "@material-ui/core/Box";
import { makeStyles } from "@material-ui/core/styles";
import Container from "@material-ui/core/Container";
import logo from "../../static/grab.png";
import SearchForm from "../Search";
import ButtonAppBar from "../../common/AppBar";
import Copyright from "../../common/Copyright";

const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  logo: {
    maxHeight: 200,
    maxWidth: 320,
  },
}));

export default function Home() {
  const classes = useStyles();

  return (
    <>
      <ButtonAppBar />
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <div className={classes.paper}>
          <img src={logo} className={classes.logo} alt={"logo"} />
          <SearchForm />
        </div>
        <Box mt={8}>
          <Copyright />
        </Box>
      </Container>
    </>
  );
}

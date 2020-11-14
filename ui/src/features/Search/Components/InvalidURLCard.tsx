import React from "react";
import Alert from "@material-ui/lab/Alert";
import IconButton from "@material-ui/core/IconButton";
import ReplayIcon from "@material-ui/icons/Replay";

export function InvalidUrlCard() {
  return (
    <div style={{ marginTop: "20%" }}>
      <Alert
        severity="warning"
        action={
          <IconButton
            aria-label="close"
            color="inherit"
            size="small"
            onClick={() => {
              window.location.reload();
            }}
          >
            <ReplayIcon fontSize="inherit" />
          </IconButton>
        }
      >
        Invalid Youtube URL
      </Alert>
    </div>
  );
}

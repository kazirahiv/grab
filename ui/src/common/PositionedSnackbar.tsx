import React from 'react';
import Button from '@material-ui/core/Button';
import Snackbar, { SnackbarOrigin } from '@material-ui/core/Snackbar';

export interface State extends SnackbarOrigin {
  open: boolean;
}

export interface SnackHandler {
    open : boolean,
    vertical: "top" | "bottom",
    horizontal: "left" | "center" | "right",
    message : string,
}

export default function PositionedSnackbar(handler : SnackHandler) {

  const [state, setState] = React.useState<State>({
    open: true,
    vertical: handler.vertical,
    horizontal: handler.horizontal,
  });

  const { vertical, horizontal, open } = state;

  const handleClick = (newState: SnackbarOrigin) => () => {
    setState({ open: true, ...newState });
  };

  const handleClose = () => {
    setState({ ...state, open: false });
  };
  return (
    <div>
      <Snackbar
        anchorOrigin={{ vertical, horizontal }}
        open={open}
        onClose={handleClose}
        message= {handler.message}
        key={vertical + horizontal}
      />
    </div>
  );
}

import React from 'react';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import PropTypes from 'prop-types';

GenericInfoButton.propTypes = {
    description: PropTypes.string.isRequired,
    open: PropTypes.any.isRequired,
    setOpen: PropTypes.any.isRequired,
};

export default function GenericInfoButton(props) {
    GenericInfoButton.propTypes = props.data;
    const data = props;

    const { description, open, setOpen } = data;

    //for info button
    const handleClose = () => {
        setOpen(false);
    };

    return (
        <Dialog
            open={open}
            keepMounted
            onClose={handleClose}
            aria-labelledby="alert-dialog-slide-title"
            aria-describedby="alert-dialog-slide-description"
        >
            <DialogTitle id="alert-dialog-slide-title">
                {'Information Center'}
            </DialogTitle>
            <DialogContent>
                <DialogContentText id="alert-dialog-slide-description">
                    {description}
                </DialogContentText>
            </DialogContent>
            <DialogActions>
                <Button onClick={handleClose} color="primary">
                    Okay
                </Button>
            </DialogActions>
        </Dialog>
    );
}

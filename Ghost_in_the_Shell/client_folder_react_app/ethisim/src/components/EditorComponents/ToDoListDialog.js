import React from 'react';
import {
    Dialog,
    DialogTitle,
    DialogContent,
    Button,
    Typography,
    makeStyles,
    Grid,
    Divider,
} from '@material-ui/core';
import HighlightOffIcon from '@material-ui/icons/HighlightOff';
import PropTypes from 'prop-types';

const useStyles = makeStyles((theme) => ({
    dialogWrapper: {
        padding: theme.spacing(2),
        position: 'absolute',
        top: theme.spacing(5),
    },
    exitOutButton: {
        margin: theme.spacing(2),
        marginLeft: 'auto',
        float: 'right',
        border: '3px solid',
        borderColor: theme.palette.primary.light,
    },
    root: {
        width: 'fit-content',

        backgroundColor: theme.palette.background.paper,
        color: theme.palette.text.secondary,
        '& svg': {
            margin: theme.spacing(7),
        },
        '& hr': {
            margin: theme.spacing(0, 5),
        },
    },
}));

ToDoListDialog.propTypes = {
    setOpenToDo: PropTypes.any.isRequired,
    openToDo: PropTypes.any.isRequired,
};

//REQUIRES GET ENDPOINT

export default function ToDoListDialog(props) {
    const classes = useStyles();
    ToDoListDialog.propTypes = props.data;
    const data = props;
    const { setOpenToDo, openToDo } = data;

    return (
        <div>
            <Dialog
                open={openToDo}
                maxWidth="md"
                classes={{ paper: classes.dialogWrapper }}
            >
                <DialogTitle
                    disableTypography={true}
                    style={{ display: 'flex' }}
                >
                    <Typography
                        variant="h3"
                        align="center"
                        component="div"
                        style={{ display: 'flex' }}
                    >
                        To Do List
                    </Typography>
                </DialogTitle>
                <DialogContent dividers>
                    <Grid
                        container
                        alignItems="center"
                        className={classes.root}
                    >
                        <Typography>Not Started</Typography>
                        <Divider orientation="vertical" flexItem />
                        <Typography>In Progress</Typography>
                        <Divider orientation="vertical" flexItem />
                        <Typography>Finished</Typography>
                    </Grid>
                </DialogContent>
                <Button
                    className={classes.exitOutButton}
                    variant="contained"
                    color="primary"
                    onClick={() => {
                        setOpenToDo(false);
                    }}
                >
                    <HighlightOffIcon />
                </Button>
            </Dialog>
        </div>
    );
}

import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Button, Grid } from '@material-ui/core';
import PropTypes from 'prop-types';
import GenericDeleteWarning from '../DeleteWarnings/GenericDeleteWarning';
import DeleteForeverIcon from '@material-ui/icons/DeleteForever';
import Checkbox from '@material-ui/core/Checkbox';

const useStyles = makeStyles((theme) => ({
    pageButton: {
        width: '100%',
        minHeight: '50px',
        border: '3px solid',
        borderColor: theme.palette.primary.light,
        textTransform: 'unset',
        overflowWrap: 'anywhere',
    },
    deleteButton: {
        minWidth: '40px',
        border: '3px solid',
        borderColor: theme.palette.primary.main,
        backgroundColor: theme.palette.primary.light,
    },
    deleteButtonContainer: {
        display: 'flex',
        alignItems: 'center',
    },

}));



NavSideBarNode.propTypes = {
    onClick: PropTypes.any.isRequired,
    id: PropTypes.number.isRequired,
    title: PropTypes.string.isRequired,
    deleteByID: PropTypes.any.isRequired,
    component: PropTypes.any,
    scenarioPages: PropTypes.any,
    isIntroPage: PropTypes.bool,
};

export default function NavSideBarNode(props) {
    const classes = useStyles();
    const {
        onClick,
        deleteByID,
        id,
        title,
        scenarioPages,
        isIntroPage,
    } = props;

    //Used for the popup delete warning
    const [open, setOpen] = React.useState(false);
    const handleClickOpen = () => {
        setOpen(true);
    };

    //for checkboxes
    const [checked, setChecked] = React.useState(true);
    const handleChange = (event) => {
        setChecked(event.target.checked);
      };
    
    

    function pageType(title) {
        if (id === -1 || id === -2 || id === -3 || id === -4 || isIntroPage) { //logistics to introduction pages
            return (
                
                <Grid container direction="row" justify="flex-start">
                    <Grid item xs={2} >
                        <Checkbox
                            checked={checked}
                            onChange={handleChange}
                            color = "primary"
                            inputProps={{ 'aria-label': 'primary checkbox' }}
                        />
                    </Grid>
                    <Grid item xs={8}>
                        <Button
                            className={classes.pageButton}
                            variant="contained"
                            color="primary"
                            onClick={handleDisplayComponent}
                        >
                            {title}
                        </Button>
                    </Grid>
                </Grid>
            );
        } else { //additional created pages
            return (
                <Grid container direction="row" justify="flex-start"> 
                    <Grid item xs={2}>
                        <Checkbox
                            checked={checked}
                            onChange={handleChange}
                            color = "primary"
                            inputProps={{ 'aria-label': 'primary checkbox' }}
                        />
                    </Grid>
                    <Grid item xs={8}>
                        <Button
                            className={classes.pageButton}
                            variant="contained"
                            color="primary"
                            onClick={handleDisplayComponent}
                        >
                            {title}
                        </Button>
                    </Grid>
                    <Grid item xs={2} className={classes.deleteButtonContainer}>
                        <Button
                            className={classes.deleteButton}
                            color="primary"
                            onClick={handleClickOpen}
                        >
                            <DeleteForeverIcon />
                        </Button>
                        <GenericDeleteWarning
                            remove={() => deleteByID(id)}
                            open={open}
                            setOpen={setOpen}
                        />
                    </Grid>
                </Grid>
            );
        }
    }

    function handleDisplayComponent() {
        onClick(id, title, scenarioPages);
    }

    return <div>{pageType(title)}</div>;
}

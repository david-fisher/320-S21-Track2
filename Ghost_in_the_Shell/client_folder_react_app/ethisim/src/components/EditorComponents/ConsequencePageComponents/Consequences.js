import React, { useState, useEffect } from 'react';
import Body from '../GeneralPageComponents/Body';

import Title from '../GeneralPageComponents/Title';
import {
    Typography,
    Container,
    Button,
    Grid,
    TextField,
} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import PropTypes from 'prop-types';
import universalPost from '../../../universalHTTPRequests/post.js';
import universalDelete from '../../../universalHTTPRequests/delete.js';
import SuccessBanner from '../../Banners/SuccessBanner';
import ErrorBanner from '../../Banners/ErrorBanner';
import LoadingSpinner from '../../LoadingSpinner';
import HelpIcon from '@material-ui/icons/Help';
import GenericInfoButton from '../../InfoButtons/GenericInfoButton';
import InformationItemList from '../GenericPageComponents/InformationItemList';
const useStyles = makeStyles((theme) => ({
    saveButton: {
        margin: theme.spacing(2),
        float: 'right',
        textTransform: 'unset',
    },
    bannerContainer: {
        marginTop: theme.spacing(1),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
}));
Consequences.propTypes = {
    scenario_ID: PropTypes.any,
    body: PropTypes.any,
};
export default function Consequences(props) {
    const { scenario_ID, body } = props;

    const classes = useStyles();
    //for info button
    const [open, setOpen] = React.useState(false);
    const handleClickOpen = () => {
        setOpen(true);
    };

    //for text body
    const [bodyText, setBodyText] = useState(body);

    return (
        /*<Container component="main">
            <Typography align="center" variant="h2">
                Consequences
            </Typography>
            {<Grid container justify="flex-end">
                <Button color="primary" onClick={handleClickOpen}>
                    <HelpIcon />
                </Button>
                <GenericInfoButton
                    description={`Give the student an introduction to the ethical scenario. What is the problem? Think about both the positive and negative potential consequences of the technology,
                    as well as the stakeholders who are promoting the technology and the stakeholders who will be most directly impacted.
                    `}
                    open={open}
                    setOpen={setOpen}
                />
            </Grid>
            <Title
                title={title}
                setTitle={setTitle}
                error={errorTitle}
                errorMessage={errorTitleText}
            />
            <Body
                body={bodyText}
                setBody={setBodyText}
                error={errorBody}
                errorMessage={'Page body cannot be empty.'}
            />
            <Button
                className={classes.saveButton}
                variant="contained"
                color="primary"
                //onClick={savePage}
            >
                Save
    </Button> }
        </Container>
    );*/
    <div>
            <Typography align="center" variant="h2">
                Consequences
            </Typography>
            <Title />
            <Body />
           
            <Button variant="contained" color="grey">
                Save Consequence
            </Button>
           
        </div>
    )
}

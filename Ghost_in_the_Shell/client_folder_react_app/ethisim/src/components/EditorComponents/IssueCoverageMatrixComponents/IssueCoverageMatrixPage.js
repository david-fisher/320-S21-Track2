import React, { useState, useEffect, useRef } from 'react';
import {
    Typography,
    Button,
    Grid,
    TextField,
    MenuItem,
    Dialog,
    DialogTitle,
    DialogContent,
    DialogContentText,
    DialogActions,
} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import EntryFields from './IssueEntryFieldList';
import get from '../../../universalHTTPRequests/get';
import LoadingSpinner from '../../LoadingSpinner';
import RefreshIcon from '@material-ui/icons/Refresh';
import ErrorIcon from '@material-ui/icons/Error';
import PropTypes from 'prop-types';
import IssueMatrix from './IssueCoverageMatrix';
import { baseURL } from '../../../Constants/Config';

import MaterialTable from 'material-table';
import addStakeHolder from '../ConversationEditorComponents/StakeHoldersComponent/stakeHolders';
//import saveStakeHolder from '../ConversationEditorComponents/StakeHoldersComponent/stakeHolders';
//import saveStakeHolders from 'ethisim/src/components/EditorComponents/ConversationEditorComponents/StakeHoldersComponent/stakeHolders.js'
import HelpIcon from '@material-ui/icons/Help';
import GenericInfoButton from '../../InfoButtons/GenericInfoButton';

//Need scenarioID
const endpointGET = '/api/issues/?SCENARIO=';

const useStyles = makeStyles((theme) => ({
    issue: {
        marginTop: theme.spacing(2),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    spacing: {
        padding: theme.spacing(1),
    },
    saveButton: {
        margin: theme.spacing(2),
        float: 'right',
        textTransform: 'unset',
    },
    container: {
        padding: theme.spacing(1),
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
    },
    iconError: {
        paddingRight: theme.spacing(2),
        fontSize: '75px',
    },
    iconRefreshLarge: {
        fontSize: '75px',
    },
    iconRefreshSmall: {
        fontSize: '30px',
    },
}));

ICMatrix.propTypes = {
    scenario_ID: PropTypes.number,
};

export default function ICMatrix({ scenario_ID }) {
    const [open, setOpen] = React.useState(false);
    const handleClickOpen = () => {
        setOpen(true);
    };
    const handleClose = () => {
        setOpen(false);
    };
    const classes = useStyles();
    const [issueEntryFieldList, setIssueEntryFieldList] = useState({
        data: null,
        loading: true,
        error: null,
    });
    const [issueCoverageMatrix, setIssueCoverageMatrix] = useState({
        data: null,
        loading: true,
        error: null,
    });

    //for info button
    const [openHelp, setOpenHelp] = React.useState(false);
    const handleClickOpenHelp = () => {
        setOpenHelp(true);
    };

    const stakeHolders = useRef(null);
    const [isLoading, setLoading] = useState(false); //stores status of whether something is loading

    var axios = require('axios'); //backend
    const [successBannerMessage, setSuccessBannerMessage] = useState(''); //success banner
    const [successBannerFade, setSuccessBannerFade] = useState(false);
    const [errorBannerMessage, setErrorBannerMessage] = useState(''); //error banner
    const [errorBannerFade, setErrorBannerFade] = useState(false);

    useEffect(() => {
        getData();
    }, [stakeHolders]);

    let getData = () => {
        //getExistingStakeHolders()
        get(setIssueEntryFieldList, endpointGET + scenario_ID);
        get(setIssueCoverageMatrix, endpointGET + scenario_ID);
    };

    useEffect(() => {
        stakeHolders.current = [];
        getExistingStakeHolders();
        getData();
    }, []);

    if (issueCoverageMatrix.loading || issueEntryFieldList.loading) {
        return <LoadingSpinner />;
    }

    if (issueEntryFieldList.error) {
        return (
            <div className={classes.issue}>
                <div className={classes.container}>
                    <ErrorIcon className={classes.iconError} />
                    <Typography align="center" variant="h3">
                        Error in fetching issues.
                    </Typography>
                </div>
                <Button variant="contained" color="primary" onClick={getData}>
                    <RefreshIcon className={classes.iconRefreshLarge} />
                </Button>
            </div>
        );
    }

    function onStakeHolderChange(childData) {
        getExistingStakeHolders();
    }

    /*<IssueMatrix onChange = {this.onStakeHolderChange}/>*/

    function getExistingStakeHolders() {
        setLoading(true); //starts loading icon

        var data = { SCENARIO: { scenario_ID } };
        var config = {
            method: 'get',
            url: baseURL + '/stakeholder?scenario_id=' + scenario_ID,
            headers: {
                'Content-Type': 'application/json',
            },
            data: data,
        };

        axios(config) //backend call to get data in response
            .then(function (response) {
                stakeHolders.current = response.data;
                setLoading(false);
            })
            .catch(function (error) {
                setErrorBannerMessage(
                    'Failed to get Stakeholders! Please try again.'
                );
                setErrorBannerFade(true);
            });
    }

    /* <EntryFields
            issueEntryFieldList={
                issueEntryFieldList !== null ? issueEntryFieldList : []
            }
            setIssueEntryFieldList={setIssueEntryFieldList}
            scenarioID={scenario_ID}
    />*/

    /*return (
        <div className={classes.issue}>
            <Typography align="center" variant="h2">
                Configure Ethical Issues
            </Typography>
            <div className={classes.spacing}>
                <Button variant="contained" color="primary" onClick={getData}>
                    <RefreshIcon className={classes.iconRefreshSmall} />
                </Button>
            </div>
            <MaterialTable>
                issueCoverageMatrix = {issueCoverageMatrix}
                setIssueCoverageMatrix = {setissueCoverageMatrix}
            </MaterialTable>
        </div>
    );*/
    //for info button

    if (isLoading) {
        return <LoadingSpinner />;
    }

    return (
        <div className={classes.issue}>
            <Typography align="center" variant="h2">
                Configure Coverage Scores
            </Typography>
            <Grid container justify="flex-end">
                <Button color="primary" onClick={handleClickOpenHelp}>
                    <HelpIcon />
                </Button>
                <GenericInfoButton
                    description={`This page is currently under maintenance.`}
                    open={openHelp}
                    setOpen={setOpenHelp}
                />
            </Grid>
            <div className={classes.spacing}>
                <Button variant="contained" color="primary" onClick={getData}>
                    <RefreshIcon className={classes.iconRefreshSmall} />
                </Button>
            </div>

            <EntryFields
                issueEntryFieldList={
                    issueEntryFieldList !== null ? issueEntryFieldList : []
                }
                setIssueEntryFieldList={setIssueEntryFieldList}
                scenario_stakeHolders={stakeHolders}
                scenarioID={scenario_ID}
            />

            <Button
                className={classes.button}
                id="button"
                onClick={handleClickOpen}
                variant="contained"
                color="primary"
            >
                {' '}
                Add Stakeholders
            </Button>

            <Dialog
                open={open}
                onClose={handleClose}
                aria-labelledby=""
                aria-describedby=""
            >
                <DialogTitle id="Add stakeholder">
                    {'Add Stakeholder'}
                </DialogTitle>
                <Grid container direction="row" justify="centre">
                    <Grid item xs={8}>
                        <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            name="StakeHolder name"
                            label="Stakeholder name"
                            id="scenariopageAdder"
                            // onChange={(e)=>addStakeholder(e)}
                        ></TextField>

                        <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            name="Job"
                            label="Job"
                            id="scenariopageAdder"
                            onChange={(e) => null}
                        ></TextField>

                        <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            name="Description"
                            label="Description"
                            id="scenariopageAdder"
                        ></TextField>
                        <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            name="Bio"
                            label="Bio"
                            id="scenariopageAdder"
                        ></TextField>
                    </Grid>
                </Grid>
                <DialogActions>
                    <Button onClick={handleClose} color="primary">
                        Done
                    </Button>
                </DialogActions>
            </Dialog>

            <IssueMatrix /*this might need to be edited, sends scenario id to IssueCoverageMatrix*/
                scenario_stakeHolders={stakeHolders.current}
                scenario={scenario_ID}
            />
        </div>
    );
}

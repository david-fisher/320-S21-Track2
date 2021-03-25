import React, { useState, useEffect } from 'react';
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
import MaterialTable from 'material-table';
import addStakeHolder from '../ConversationEditorComponents/StakeHoldersComponent/stakeHolders';

//import saveStakeHolder from '../ConversationEditorComponents/StakeHoldersComponent/stakeHolders';

// import saveStakeHolders from 'ethisim/src/components/EditorComponents/ConversationEditorComponents/StakeHoldersComponent/stakeHolders.js'

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

ConfigureIssues.propTypes = {
    scenario_ID: PropTypes.number,
};

export default function ConfigureIssues({ scenario_ID }) {
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

    let getData = () => {
        get(setIssueEntryFieldList, endpointGET + scenario_ID);
        get(setIssueCoverageMatrix, endpointGET + scenario_ID);
    };

    useEffect(getData, []);

    if (issueEntryFieldList.loading) {
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

    return (
        <div className={classes.issue}>
            <Typography align="center" variant="h2">
                Configure Ethical Issues
            </Typography>

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
                scenario={scenario_ID}
            />
        </div>
    );
}

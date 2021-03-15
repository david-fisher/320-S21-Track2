import React, { useState, useEffect } from 'react';
import { makeStyles, withStyles } from '@material-ui/core/styles';
import {
    Container,
    Box,
    Button,
    Typography,
    CssBaseline,
    AppBar,
    Toolbar,
} from '@material-ui/core';
import PropTypes from 'prop-types';
import MaterialTable from 'material-table';
import { forwardRef } from 'react';
import { Link } from 'react-router-dom';
import get from '../../../universalHTTPRequests/get';
import LoadingSpinner from '../../LoadingSpinner';
import SuccessBanner from '../../Banners/SuccessBanner';
import ErrorBanner from '../../Banners/ErrorBanner';
import RefreshIcon from '@material-ui/icons/Refresh';
import ErrorIcon from '@material-ui/icons/Error';
import { useLocation } from 'react-router-dom';
import { baseURL } from '../../../Constants/Config';
import AddBox from '@material-ui/icons/AddBox';
import ArrowDownward from '@material-ui/icons/ArrowDownward';
import Check from '@material-ui/icons/Check';
import ChevronLeft from '@material-ui/icons/ChevronLeft';
import ChevronRight from '@material-ui/icons/ChevronRight';
import Clear from '@material-ui/icons/Clear';
import DeleteOutline from '@material-ui/icons/DeleteOutline';
import Edit from '@material-ui/icons/Edit';
import FilterList from '@material-ui/icons/FilterList';
import FirstPage from '@material-ui/icons/FirstPage';
import LastPage from '@material-ui/icons/LastPage';
import Remove from '@material-ui/icons/Remove';
import SaveAlt from '@material-ui/icons/SaveAlt';
import Search from '@material-ui/icons/Search';
import ViewColumn from '@material-ui/icons/ViewColumn';
import RateReviewIcon from '@material-ui/icons/RateReview';

const tableIcons = {
    Add: forwardRef((props, ref) => <AddBox {...props} ref={ref} />),
    Check: forwardRef((props, ref) => <Check {...props} ref={ref} />),
    Clear: forwardRef((props, ref) => <Clear {...props} ref={ref} />),
    Delete: forwardRef((props, ref) => <DeleteOutline {...props} ref={ref} />),
    DetailPanel: forwardRef((props, ref) => (
        <ChevronRight {...props} ref={ref} />
    )),
    Edit: forwardRef((props, ref) => <Edit {...props} ref={ref} />),
    Filter: forwardRef((props, ref) => <FilterList {...props} ref={ref} />),
    FirstPage: forwardRef((props, ref) => <FirstPage {...props} ref={ref} />),
    LastPage: forwardRef((props, ref) => <LastPage {...props} ref={ref} />),
    NextPage: forwardRef((props, ref) => <ChevronRight {...props} ref={ref} />),
    PreviousPage: forwardRef((props, ref) => (
        <ChevronLeft {...props} ref={ref} />
    )),
    ResetSearch: forwardRef((props, ref) => <Clear {...props} ref={ref} />),
    Search: forwardRef((props, ref) => <Search {...props} ref={ref} />),
    SortArrow: forwardRef((props, ref) => (
        <ArrowDownward {...props} ref={ref} />
    )),
    ThirdStateCheck: forwardRef((props, ref) => (
        <Remove {...props} ref={ref} />
    )),
    ViewColumn: forwardRef((props, ref) => <ViewColumn {...props} ref={ref} />),
    RateReview: forwardRef((props, ref) => (
        <RateReviewIcon {...props} ref={ref} />
    )),
};

const useStyles = makeStyles((theme) => ({
    container: {
        marginTop: theme.spacing(12),
        textAlign: 'center',
    },
    button: {
        marginBottom: theme.spacing(1),
        textTransform: 'unset',
    },
    exitButton: {
        margin: theme.spacing(2),
        borderStyle: 'solid',
        borderColor: 'white',
        border: 2,
    },
    title: {
        textAlign: 'center',
    },
    issue: {
        marginTop: theme.spacing(2),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    errorContainer: {
        marginTop: theme.spacing(2),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
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

IssueMatrix.propTypes = {
    stakeHolders: PropTypes.any,
    setStakeHolders: PropTypes.any,
    scenario: PropTypes.number,
};

//Needs scenario id
const endpointGET = '/student_info?scenario_id=';

export default function IssueMatrix({ scenario }) {
    //receives the scenario ID
    const classes = useStyles();

    const [didGetSHs, setDidGetSHs] = useState(false); //stores status of whether stakeholders have been received
    const [stakeHolders, setStakeHolders] = useState([]); //stores stakeholders
    const [isLoading, setLoading] = useState(false); //stores status of whether something is loading
    var axios = require('axios'); //backend

    const [successBannerMessage, setSuccessBannerMessage] = useState(''); //success banner
    const [successBannerFade, setSuccessBannerFade] = useState(false);

    useEffect(() => {
        //sets behaviour of success banner
        const timeout = setTimeout(() => {
            setSuccessBannerFade(false);
        }, 1000);

        return () => clearTimeout(timeout);
    }, [successBannerFade]);

    const [errorBannerMessage, setErrorBannerMessage] = useState(''); //error banner
    const [errorBannerFade, setErrorBannerFade] = useState(false);

    useEffect(() => {
        //sets behaviour of error banner
        const timeout = setTimeout(() => {
            setErrorBannerFade(false);
        }, 1000);

        return () => clearTimeout(timeout);
    }, [errorBannerFade]);

    function getExistingStakeHolders() {
        setLoading(true); //starts loading icon

        var data = { SCENARIO: { scenario } };
        var config = {
            method: 'get',
            url: baseURL + '/api/stakeholders/?SCENARIO=' + scenario,
            headers: {
                'Content-Type': 'application/json',
            },
            data: data,
        };

        axios(config) //backend call to get data in response
            .then(function (response) {
                setStakeHolders(response.data);
            })
            .catch(function (error) {
                setErrorBannerMessage(
                    'Failed to get Stakeholders! Please try again.'
                );
                setErrorBannerFade(true);
            });

        setLoading(false);
    }

    if (isLoading) {
        return <LoadingSpinner />;
    }

    if (!didGetSHs) {
        //if stakeholders have alreasdy been loaded, don't do it again
        setDidGetSHs(true);
        getExistingStakeHolders();
    }

    return (
        <Container component="main" className={classes.container}>
            <MaterialTable /*table*/
                icons={tableIcons} /*all the icons*/
                title={'Issue Coverage Matrix'}
                cellEditable={{
                    /*sets the cells to be editable*/ cellStyle: {},
                    onCellEditApproved: (
                        newValue,
                        oldValue,
                        rowData,
                        columnDef
                    ) => {
                        return new Promise((resolve, reject) => {
                            console.log('newValue: ' + newValue);
                            setTimeout(resolve, 4000);
                        });
                    },
                }}
                columns={[
                    { title: 'Name', field: 'NAME' },
                    { title: 'Description', field: 'DESCRIPTION' },
                ]}
                data={stakeHolders.map((
                    stakeHolder /*populates the NAME and DESCRIPTION field with stakeholder data*/
                ) => ({
                    NAME: stakeHolder.NAME,
                    DESCRIPTION: stakeHolder.DESCRIPTION,
                }))}
            />
        </Container>
    );
}

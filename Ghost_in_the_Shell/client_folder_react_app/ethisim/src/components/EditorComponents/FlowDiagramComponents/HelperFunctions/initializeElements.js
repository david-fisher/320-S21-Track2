export default function initializeElements(componentData) {
    switch (componentData.page_type) {
        case 'I':
            return {
                id: componentData.page,
                type: 'introNode',
                data: { label: componentData.page_title },
                style: {
                    border: '3px solid orange',
                    borderRadius: '5%',
                    padding: 10,
                },
                position: {
                    x: componentData.x_coordinate,
                    y: componentData.y_coordinate,
                },
                ...componentData,
            };
        case 'A':
            return {
                id: componentData.page,
                type: 'actionNode',
                data: { label: componentData.page_title },
                style: {
                    border: '3px solid green',
                    borderRadius: '5%',
                    padding: 10,
                },
                position: {
                    x: componentData.x_coordinate,
                    y: componentData.y_coordinate,
                },
                ...componentData,
            };
        case 'G':
            return {
                id: componentData.page,
                type: 'genericNode',
                data: { label: componentData.page_title },
                style: {
                    border: '3px solid red',
                    borderRadius: '5%',
                    padding: 10,
                },
                position: {
                    x: componentData.x_coordinate,
                    y: componentData.y_coordinate,
                },
                ...componentData,
            };
        case 'R':
            return {
                id: componentData.page,
                type: 'reflectionNode',
                data: { label: componentData.page_title },
                style: {
                    border: '3px solid purple',
                    borderRadius: '5%',
                    padding: 10,
                },
                position: {
                    x: componentData.x_coordinate,
                    y: componentData.y_coordinate,
                },
                ...componentData,
            };
        case 'S':
            return {
                id: componentData.page,
                type: 'conversationNode',
                data: { label: componentData.page_title },
                style: {
                    border: '3px solid blue',
                    borderRadius: '5%',
                    padding: 10,
                },
                position: {
                    x: componentData.x_coordinate,
                    y: componentData.y_coordinate,
                },
                ...componentData,
            };
        default:
            return {
                id: componentData.page,
                type: 'conversationNode',
                data: { label: componentData.page_title },
                style: {
                    border: '3px solid blue',
                    borderRadius: '5%',
                    padding: 10,
                },
                position: {
                    x: componentData.x_coordinate,
                    y: componentData.y_coordinate,
                },
                ...componentData,
            };
    }
}

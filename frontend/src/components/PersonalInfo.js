
function PersonalInfo(props) {
    const user = props.user;

    return (
        <span>
            Hello {user.name}! Balance: {user.balance}$
        </span>
    );
}

export default PersonalInfo;
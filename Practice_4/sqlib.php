<?php

if( isset( $_GET[ 'Submit' ] ) ) {
        // Check Anti-CSRF token
        checkToken( $_REQUEST[ 'user_token' ], $_SESSION[ 'session_token' ], 'index.php' );
        $exists = false;

        // Get input
        $id = $_GET[ 'id' ];

        // Was a number entered?
        if(is_numeric( $id )) {
                $id = intval ($id);
                $_DVWA['MYSQL'])
                      // Check the database
                      $data = $db->prepare( 'SELECT first_name, last_name FROM users WHERE user_id = (:id) LIMIT 1;' );
                      $data->bindParam( ':id', $id, PDO::PARAM_INT );
                      $data->execute();

                      $exists = $data->rowCount();
                      break;
        }

        // Get results
        if ($exists) {
                // Feedback for end user
                $html .= '<pre>User ID exists in the database.</pre>';
        } else {
                // User wasn't found, so the page wasn't!
                header( $_SERVER[ 'SERVER_PROTOCOL' ] . ' 404 Not Found' );

                // Feedback for end user
                $html .= '<pre>User ID is MISSING from the database.</pre>';
        }
}

// Generate Anti-CSRF token
generateSessionToken();

?>

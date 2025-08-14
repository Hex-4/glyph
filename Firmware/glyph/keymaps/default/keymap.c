#include QMK_KEYBOARD_H

enum layers {
    _BASE = 0,
    _SYMBOLS,
    _NUMBERS,
    _FUNCTION
};

// Tap Dance declarations
enum {
    CG,
    EW,
};

// Tap Dance definitions
tap_dance_action_t tap_dance_actions[] = {
    [CG] = ACTION_TAP_DANCE_DOUBLE(KC_LCTL, KC_LGUI),
    [EW] = ACTION_TAP_DANCE_DOUBLE(KC_ESC, CW_TOGG),
};



const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * Base Layer (QWERTY-ish for programming)
     * ┌───┬───┬───┬───┬───┬───┐       ┌───┬───┬───┬───┬───┬───┐
     * │E/W│ Q │ W │ E │ R │ T │       │ Y │ U │ I │ O │ P │Bsp│
     * ├───┼───┼───┼───┼───┼───┤       ├───┼───┼───┼───┼───┼───┤
     * │Tab│ A │ S │ D │ F │ G │       │ H │ J │ K │ L │ ; │ ' │
     * ├───┼───┼───┼───┼───┼───┤       ├───┼───┼───┼───┼───┼───┤
     * │C/G│ Z │ X │ C │ V │ B │       │ N │ M │ , │ . │ / │Ent│
     * └───┴───┴───┴───┴───┴───┘       └───┴───┴───┴───┴───┴───
     *               ┌─────────┐       ┌─────────┐
     *               │Spc/Shft │       │Sym Layer│
     *               └─────────┘       └─────────┘
     */
    [_BASE] = LAYOUT(
        TD(EW),  KC_Q,    KC_W,    KC_E,    KC_R,    KC_T,         KC_Y,    KC_U,    KC_I,    KC_O,    KC_P,    KC_BSPC,
        KC_TAB,  KC_A,    KC_S,    KC_D,    KC_F,    KC_G,         KC_H,    KC_J,    KC_K,    KC_L,    KC_SCLN, KC_QUOT,
        TD(CG),  KC_Z,    KC_X,    KC_C,    KC_V,    KC_B,         KC_N,    KC_M,    KC_COMM, KC_DOT,  KC_SLSH, KC_ENT,
                                            LSFT_T(KC_SPC),        MO(_SYMBOLS)
    ),

    /*
     * Symbols Layer (Programming symbols and brackets)
     *
     * ┌───┬───┬───┬───┬───┬───┐       ┌───┬───┬───┬───┬───┬───┐
     * │ ` │ 1 │ 2 │ 3 │ 4 │ 5 │       │ 6 │ 7 │ 8 │ 9 │ 0 │Del│
     * ├───┼───┼───┼───┼───┼───┤       ├───┼───┼───┼───┼───┼───┤
     * │   │ up│Prt│ [ │ ] │ \ │       │ ( │ ) │ - │ = │ : │ " │
     * ├───┼───┼───┼───┼───┼───┤       ├───┼───┼───┼───┼───┼───┤
     * │lft│dwn│rgt│ { │ } │ | │       │PgU│PgD│ < │ > │ ? │FNC│
     * └───┴───┴───┴───┴───┴───┘       └───┴───┴───┴───┴───┴───┘
     *               ┌─────────┐       ┌─────────┐
     *               │   Ctrl  │       │ ■■■■■■■ │
     *               └─────────┘       └─────────┘
     */
    [_SYMBOLS] = LAYOUT(
        KC_GRV,  KC_1   , KC_2 ,   KC_3   , KC_4  ,  KC_5   ,      KC_6   , KC_7   , KC_8   , KC_9   , KC_0   , KC_DEL,
        TD(CG) , KC_UP  , KC_PSCR, KC_LBRC, KC_RBRC, KC_BSLS,      KC_LPRN, KC_RPRN, KC_MINS, KC_EQL , KC_COLN, KC_DQUO,
        KC_LEFT, KC_DOWN, KC_RGHT, KC_LCBR, KC_RCBR, KC_PIPE,      KC_PGUP, KC_PGDN, KC_LABK, KC_RABK, KC_QUES, TG(_FUNCTION),
                                            _______,               _______
    ),
    /*
     * Function Layer (System controls, media, etc.)
     * ┌───┬───┬───┬───┬───┬───┐       ┌───┬───┬───┬───┬───┬───┐
     * │Rst│   │   │   │   │   │       │   │   │   │   │   │   │
     * ├───┼───┼───┼───┼───┼───┤       ├───┼───┼───┼───┼───┼───┤
     * │UG?│   │H+ │S+ │V+ │SP+│       │AS+│AS?│ASR│   │   │   │
     * ├───┼───┼───┼───┼───┼───┤       ├───┼───┼───┼───┼───┼───┤
     * │UG-│UG+│H- │S- │V- │SP-│       │AS-│Mut│V- │V+ │   │   │
     * └───┴───┴───┴───┴───┴───┘       └───┴───┴───┴───┴───┴───┘
     *               ┌─────────┐       ┌─────────┐
     *               │         │       │         │
     *               └─────────┘       └─────────┘
     */
    [_FUNCTION] = LAYOUT(
        QK_BOOT, _______, _______, _______, _______, _______,      _______, _______, _______, _______, _______, _______,
        UG_TOGG, _______, UG_HUEU, UG_SATU, UG_VALU, UG_SPDU,      AS_UP  , AS_TOGG, AS_RPT , _______, _______, _______,
        UG_PREV, UG_NEXT, UG_HUED, UG_SATD, UG_VALD, UG_SPDD,      AS_DOWN, KC_MUTE, KC_VOLD, KC_VOLU, _______, _______,
                                            _______,               _______
    )
};


void keyboard_post_init_user(void) {
    debug_enable=true; 
    debug_matrix=true;
    debug_keyboard=true;
    debug_mouse=true;
};
static int prev_direction = 0;  // 0=center, 1=up, 2=down, 3=left, 4=right

static int prev_prev_direction = 0;

static int prev_prev_prev_direction = 0;

int get_direction(int x, int y) {
    if (abs(x) < 2 && abs(y) < 2) return 0;
    
    if (abs(y) > abs(x)) {
        return (y > 0) ? 2 : 1;
    } else {
        return (x > 0) ? 3 : 4;
    }
}

report_mouse_t pointing_device_task_combined_user(report_mouse_t left_report, report_mouse_t right_report) {
    // Left side for scrolling
    left_report.h = left_report.x * 0.1;
    left_report.v = left_report.y * 0.1;
    left_report.x = 0;
    left_report.y = 0;
    
    // Right side for directional keys
    int current_direction = get_direction(-right_report.x, right_report.y);

    if (prev_direction != 0 && prev_prev_prev_direction == prev_direction) {
        current_direction = prev_direction;
    } else if (current_direction != 0 && prev_prev_direction == current_direction) {
        prev_direction = current_direction;
    };

    if (current_direction != prev_direction) {
        
        switch (current_direction) {
            case 1: tap_code(KC_UP); break;
            case 2: tap_code(KC_DOWN); break;
            case 3: tap_code(KC_LEFT); break;
            case 4: tap_code(KC_RIGHT); break;
            case 0: break;
        }  
    };

    prev_prev_prev_direction = prev_prev_direction;
    prev_prev_direction = prev_direction;
    prev_direction = get_direction(-right_report.x, right_report.y);
    
    right_report.x = 0;
    right_report.y = 0;
    return pointing_device_combine_reports(left_report, right_report);
}